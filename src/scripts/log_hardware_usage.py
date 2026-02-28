#!/usr/bin/env python3
"""
Log system metrics every 1 second into a pandas DataFrame (memory units in GB):
- CPU usage (%)
- Virtual memory usage (used GB, available GB, percent)
- GPU utilization (%)
- GPU memory usage (used GB, total GB, percent)

Requirements:
  pip install psutil pandas
  # For GPU metrics (NVIDIA):
  # - have nvidia-smi available on PATH (comes with NVIDIA drivers)

Notes:
- If no NVIDIA GPU / nvidia-smi is unavailable, GPU fields will be NaN.
- "GB" here is decimal gigabytes (1 GB = 1e9 bytes), matching common reporting.
"""

from __future__ import annotations

import shutil
import subprocess
import time
from datetime import datetime, timezone
from typing import Dict, Optional

import pandas as pd
import psutil


BYTES_PER_GB = 1e9


def _nvidia_smi_available() -> bool:
    return shutil.which("nvidia-smi") is not None


def read_gpu_metrics_nvidia() -> Dict[str, float]:
    """
    Returns GPU metrics for GPU 0 via nvidia-smi:
      gpu_utilization_percent
      gpu_mem_used_gb
      gpu_mem_total_gb
      gpu_mem_percent
    If unavailable, returns NaNs.
    """
    keys = [
        "gpu_utilization_percent",
        "gpu_mem_used_gb",
        "gpu_mem_total_gb",
        "gpu_mem_percent",
    ]

    if not _nvidia_smi_available():
        return {k: float("nan") for k in keys}

    # Query GPU 0 only.
    cmd = [
        "nvidia-smi",
        "--query-gpu=utilization.gpu,memory.used,memory.total",
        "--format=csv,noheader,nounits",
        "-i",
        "0",
    ]

    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True).strip()
        # Example: "12, 1024, 8192" (values are in MiB for memory fields)
        parts = [p.strip() for p in out.split(",")]
        if len(parts) != 3:
            raise ValueError(f"Unexpected nvidia-smi output: {out!r}")

        util = float(parts[0])

        mem_used_mib = float(parts[1])
        mem_total_mib = float(parts[2])

        # Convert MiB -> bytes -> GB (decimal)
        mem_used_gb = (mem_used_mib * 1024**2) / BYTES_PER_GB
        mem_total_gb = (mem_total_mib * 1024**2) / BYTES_PER_GB
        mem_pct = (mem_used_gb / mem_total_gb * 100.0) if mem_total_gb > 0 else float("nan")

        return {
            "gpu_utilization_percent": util,
            "gpu_mem_used_gb": mem_used_gb,
            "gpu_mem_total_gb": mem_total_gb,
            "gpu_mem_percent": mem_pct,
        }
    except Exception:
        return {k: float("nan") for k in keys}


def sample_metrics() -> Dict[str, float]:
    """
    Take one sample of all metrics and return a flat dict suitable for a DataFrame row.
    """
    cpu_percent = psutil.cpu_percent(interval=None)

    vm = psutil.virtual_memory()
    vmem_used_gb = vm.used / BYTES_PER_GB
    vmem_available_gb = vm.available / BYTES_PER_GB

    gpu = read_gpu_metrics_nvidia()

    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "cpu_percent": float(cpu_percent),
        "vmem_used_gb": float(vmem_used_gb),
        "vmem_available_gb": float(vmem_available_gb),
        "vmem_percent": float(vm.percent),
        "gpu_utilization_percent": float(gpu["gpu_utilization_percent"]),
        "gpu_mem_used_gb": float(gpu["gpu_mem_used_gb"]),
        "gpu_mem_total_gb": float(gpu["gpu_mem_total_gb"]),
        "gpu_mem_percent": float(gpu["gpu_mem_percent"]),
    }


def log_hardware_metrics(duration_seconds: Optional[int] = None, interval_seconds: float = 1.0) -> pd.DataFrame:
    """
    Log metrics every `interval_seconds`.
    - If duration_seconds is None: runs until Ctrl+C.
    - Else: runs for ~duration_seconds and returns the DataFrame.
    """
    rows = []

    # Prime CPU percent so the first reported value is meaningful
    psutil.cpu_percent(interval=None)

    t0 = time.time()
    try:
        while True:
            if duration_seconds is not None and (time.time() - t0) >= duration_seconds:
                break

            rows.append(sample_metrics())
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        pass

    df = pd.DataFrame(rows)
    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], utc=True)
    return df


if __name__ == "__main__":
    df = log_hardware_metrics(duration_seconds=3600.0, interval_seconds=5.0)
    print(df.tail())

    df.to_csv("hardware_metrics_log.csv", index=False)
    print("Saved to hardware_metrics_log.csv")
