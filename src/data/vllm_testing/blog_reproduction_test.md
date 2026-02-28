# Testing results of vLLM on local machine

This README contains the reproduced results of LLM inference performance in [How Speculative Decoding Boosts vLLM Performance by up to 2.8x, 2024](https://blog.vllm.ai/2024/10/17/spec-decode.html
).

## Designated Setup

| Item                         | Value                          |
| ---------------------------- | ------------------------------ |
| Target model                 | facebook/opt-6.7b              |
| Draft model                  | facebook/opt-125m              |
| GPU                          | NVIDIA RTX 4060 Ti (16GB VRAM) |

## Vanilla

| Metric                   | Test 1  |
|--------------------------|---------|
|Total run time (sec)      | 640.86  |
|Total tokens generated    | 20205   |
|Throughput (tokens/sec)   | 31.53   |
|Throughput (requests/sec) | 0.016   |

Note: Here we only run inference for 10 requests because of the long run time.

## Speculative Decoding

| Metric                   | Test 1  |
|--------------------------|---------|
|Total run time (sec)      | 212.13  |
|Total tokens generated    | 20205   |
|Throughput (tokens/sec)   | 95.25   |
|Throughput (requests/sec) | 0.047   |

Note: Here we only run inference for 10 requests because of the long run time.
