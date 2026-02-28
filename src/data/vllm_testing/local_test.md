# Testing results of vLLM on local machine

This README contains the testing results of vLLM on a local machine with NVIDIA RTX 4060 Ti GPU. The tests are conducted on the Qwen/Qwen3-4B model and its pre-quantized version, Qwen/Qwen3-4B-AWQ. The results include various metrics such as total run time, total tokens generated, throughput in tokens per second, and throughput in requests per second. The tests also cover different configurations, including vanilla, prompt engineering, speculative decoding, quantization, and combinations of these techniques.

## Designated Setup

| Item                         | Value                          |
| ---------------------------- | ------------------------------ |
| Target model                 | Qwen/Qwen3-4B                  |
| Target model (Pre-quantized) | Qwen/Qwen3-4B-AWQ              |
| Draft model                  | Qwen/Qwen3-0.6B                |
| GPU                          | NVIDIA RTX 4060 Ti (16GB VRAM) |

## Vanilla

| Metric                   | Test 1 | Test 2 | Test 3 |
|--------------------------|--------|--------|--------|
|Total run time (sec)      | 164.51 | 170.17 | 163.35 |
|Total tokens generated    | 51001  | 53003  | 50941  |
|Throughput (tokens/sec)   | 310.01 | 311.48 | 311.84 |
|Throughput (requests/sec) | 0.304  | 0.294  | 0.306  |

## Prompt Engineering

| Metric                   | Test 1 | Test 2 | Test 3 |
|--------------------------|--------|--------|--------|
|Total run time (sec)      | 45.67  | 44.37  | 40.70  |
|Total tokens generated    | 16558  |  16746 | 16092  |
|Throughput (tokens/sec)   | 362.59 | 377.41 | 395.34 |
|Throughput (requests/sec) | 1.095  | 1.127  | 1.228  |

## Speculative Decoding

| Metric                   | Test 1 | Test 2 | Test 3 |
|--------------------------|--------|--------|--------|
|Total run time (sec)      | 202.23 | 196.72 | 184.76 |
|Total tokens generated    | 53373  | 51990  | 50619  |
|Throughput (tokens/sec)   | 263.92 | 264.28 | 273.97 |
|Throughput (requests/sec) | 0.247  | 0.254  | 0.271  |

Note: The draft acceptance rate is around 30-50%, which means that around 30-50% of the generated drafts are accepted and used for further processing.

## Quantization (vLLM)

| Metric                   | Test 1 |
|--------------------------|--------|
|Total run time (sec)      | 332.04 |
|Total tokens generated    | 59507  |
|Throughput (tokens/sec)   | 179.21 |
|Throughput (requests/sec) | 0.151  |

Note: Only one test is conducted because of the long run time.

## Quantization (Pre-quantized model)

| Metric                   | Test 1 | Test 2 | Test 3 |
|--------------------------|--------|--------|--------|
|Total run time (sec)      | 93.02  | 89.62  | 87.09  |
|Total tokens generated    | 57761  | 57929  | 57530  |
|Throughput (tokens/sec)   | 620.93 | 646.41 | 660.62 |
|Throughput (requests/sec) | 0.537  | 0.558  | 0.574  |

## Prompt Engineering + Speculative Decoding

| Metric                   | Test 1 | Test 2 | Test 3 |
|--------------------------|--------|--------|--------|
|Total run time (sec)      | 53.25  | 50.96  | 48.93  |
|Total tokens generated    | 16390  | 16367  | 16222  |
|Throughput (tokens/sec)   | 307.80 | 321.18 | 331.55 |
|Throughput (requests/sec) | 0.939  | 0.981  | 1.022  |

Note: The draft acceptance rate is around 40-50%, slightly higher than the vanilla speculative decoding.

## Prompt Engineering + Speculative Decoding + Quantization (Pre-quantized model)

| Metric                   | Test 1 | Test 2 | Test 3 |
|--------------------------|--------|--------|--------|
|Total run time (sec)      | 37.12  | 36.80  | 38.51  |
|Total tokens generated    | 20171  | 20355  | 20125  |
|Throughput (tokens/sec)   | 543.46 | 553.18 | 522.52 |
|Throughput (requests/sec) | 1.347  | 1.359  | 1.298  |

Note: The draft acceptance rate is around 30-60%, which has larger variance.

## Prompt Engineering + Quantization (Pre-quantized model)

| Metric                   | Test 1 | Test 2 | Test 3 |
|--------------------------|--------|--------|--------|
|Total run time (sec)      | 22.34  | 23.89  | 23.90  |
|Total tokens generated    | 20272  | 20589  | 20566  |
|Throughput (tokens/sec)   | 907.42 | 861.71 | 860.87 |
|Throughput (requests/sec) | 2.238  | 2.093  | 2.093  |
