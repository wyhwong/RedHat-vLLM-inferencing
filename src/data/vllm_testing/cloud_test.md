# Testing results of vLLM on cloud machine

This README contains the testing results of vLLM on a cloud machine with NVIDIA B200 GPU. The tests are conducted on the Qwen/Qwen3-32B model and its pre-quantized version, Qwen/Qwen3-32B-AWQ. The results include various metrics such as total run time, total tokens generated, throughput in tokens per second, and throughput in requests per second. The tests also cover different configurations, including vanilla, prompt engineering, speculative decoding, quantization, and combinations of these techniques.

## Designated Setup

| Item                         | Value                    |
| ---------------------------- | ------------------------ |
| Target model                 | Qwen/Qwen3-32B           |
| Target model (Pre-quantized) | Qwen/Qwen3-32B-AWQ       |
| Draft model                  | Qwen/Qwen3-14B-AWQ       |
| GPU                          | NVIDIA B200 (180GB VRAM) |

## Vanilla

| Metric                   | Test 1  |
|--------------------------|---------|
|Total run time (sec)      | 44.99   |
|Total tokens generated    | 57373   |
|Throughput (tokens/sec)   | 1275.15 |
|Throughput (requests/sec) | 1.111   |


## Prompt Engineering

| Metric                   | Test 1  |
|--------------------------|---------|
|Total run time (sec)      | 16.96   |
|Total tokens generated    | 20746   |
|Throughput (tokens/sec)   | 1222.96 |
|Throughput (requests/sec) | 2.947   |

## Speculative Decoding

| Metric                   | Test 1  |
|--------------------------|---------|
|Total run time (sec)      | 52.52   |
|Total tokens generated    | 57302   |
|Throughput (tokens/sec)   | 1091.03 |
|Throughput (requests/sec) | 0.952   |

## Quantization (vLLM)

| Metric                   | Test 1  |
|--------------------------|---------|
|Total run time (sec)      | 112.19  |
|Total tokens generated    | 53134   |
|Throughput (tokens/sec)   | 473.59  |
|Throughput (requests/sec) | 0.446   |

## Quantization (Pre-quantized model)

| Metric                   | Test 1  |
|--------------------------|---------|
|Total run time (sec)      | 35.35   |
|Total tokens generated    | 58157   |
|Throughput (tokens/sec)   | 1645.24 |
|Throughput (requests/sec) | 1.414   |

## Prompt Engineering + Speculative Decoding

| Metric                   | Test 1  |
|--------------------------|---------|
|Total run time (sec)      | 24.99   |
|Total tokens generated    | 20726   |
|Throughput (tokens/sec)   | 829.51  |
|Throughput (requests/sec) | 2.001   |

## Prompt Engineering + Speculative Decoding + Quantization (Pre-quantized model)

| Metric                   | Test 1  |
|--------------------------|---------|
|Total run time (sec)      | 18.14   |
|Total tokens generated    | 20335   |
|Throughput (tokens/sec)   | 1121.12 |
|Throughput (requests/sec) | 2.757   |

## Prompt Engineering + Quantization (Pre-quantized model)

| Metric                   | Test 1  |
|--------------------------|---------|
|Total run time (sec)      | 15.32   |
|Total tokens generated    | 20787   |
|Throughput (tokens/sec)   | 1656.87 |
|Throughput (requests/sec) | 3.264   |
