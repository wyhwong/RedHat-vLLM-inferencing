# Setup
Target model: Qwen/Qwen3-32B
Target model (Pre-quantized): Qwen/Qwen3-32B-AWQ
Draft model: Qwen/Qwen3-8B-AWQ
GPU: NVIDIA B200 (180GB VRAM)

# Vanilla
Total run time: 44.99 seconds
Total tokens generated: 57373
Throughput (tokens/sec): 1275.15
Throughput (requests/sec): 1.111

# Prompt Engineering
Total run time: 16.96 seconds
Total tokens generated: 20746
Throughput (tokens/sec): 1222.96
Throughput (requests/sec): 2.947

# Speculative Decoding
Total run time: 52.52 seconds
Total tokens generated: 57302
Throughput (tokens/sec): 1091.03
Throughput (requests/sec): 0.952

# Quantization (vLLM)
Total run time: 112.19 seconds
Total tokens generated: 53134
Throughput (tokens/sec): 473.59
Throughput (requests/sec): 0.446

# Quantization (Pre-quantized model)
Total run time: 35.35 seconds
Total tokens generated: 58157
Throughput (tokens/sec): 1645.24
Throughput (requests/sec): 1.414

# 1+2+3
Total run time: 24.99 seconds
Total tokens generated: 20726
Throughput (tokens/sec): 829.51
Throughput (requests/sec): 2.001

# 2+3+5
Total run time: 18.14 seconds
Total tokens generated: 20335
Throughput (tokens/sec): 1121.12
Throughput (requests/sec): 2.757

# 2+5
Total run time: 15.32 seconds
Total tokens generated: 20787
Throughput (tokens/sec): 1656.87
Throughput (requests/sec): 3.264
