# Testing results of Ollama on local machine

This README contains the testing results of Ollama on a local machine with NVIDIA RTX 4060 Ti GPU. The tests are conducted on the Qwen/Qwen3-4B model. The results include various metrics such as total run time, total tokens generated, throughput in tokens per second, and throughput in requests per second.

## Designated Setup

| Item                         | Value                          |
| ---------------------------- | ------------------------------ |
| Model                        | qwen3:4b                       |
| GPU                          | NVIDIA RTX 4060 Ti (16GB VRAM) |

## Vanilla

| Metric                   | Test 1 |
|--------------------------|--------|
|Total run time (sec)      | 432.54 |
|Total tokens generated    | 72050  |
|Throughput (tokens/sec)   | 166.57 |
|Throughput (requests/sec) | 0.116  |

Note: OLLAMA_NUM_PARALLEL=4

| Metric                   | Test 1 | Test 2 |
|--------------------------|--------|--------|
|Total run time (sec)      | 344.90 | 347.31 |
|Total tokens generated    | 71655  | 75018  |
|Throughput (tokens/sec)   | 207.75 | 216.00 |
|Throughput (requests/sec) | 0.145  | 0.144  |

Note: OLLAMA_NUM_PARALLEL=8

| Metric                   | Test 1 |
|--------------------------|--------|
|Total run time (sec)      | 721.96 |
|Total tokens generated    | 74356  |
|Throughput (tokens/sec)   | 102.99 |
|Throughput (requests/sec) | 0.069  |

Note: OLLAMA_NUM_PARALLEL=12
