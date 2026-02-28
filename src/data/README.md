#### Overview

The data in this directory is generated with RTX4060ti with 16GB VRAM.
It may not be reproducible on GPUs on other machines.

# Vanilla
## Test 1
Total run time: 164.51 seconds
Total tokens generated: 51001
Throughput (tokens/sec): 310.01
Throughput (requests/sec): 0.304
## Test 2
Total run time: 170.17 seconds
Total tokens generated: 53003
Throughput (tokens/sec): 311.48
Throughput (requests/sec): 0.294
## Test 3
Total run time: 163.35 seconds
Total tokens generated: 50941
Throughput (tokens/sec): 311.84
Throughput (requests/sec): 0.306

# Prompt Engineering
## Test 1
Total run time: 45.67 seconds
Total tokens generated: 16558
Throughput (tokens/sec): 362.59
Throughput (requests/sec): 1.095
## Test 2
Total run time: 44.37 seconds
Total tokens generated: 16746
Throughput (tokens/sec): 377.41
Throughput (requests/sec): 1.127
## Test 3
Total run time: 40.70 seconds
Total tokens generated: 16092
Throughput (tokens/sec): 395.34
Throughput (requests/sec): 1.228

# Speculative Decoding
## Test 1
Total run time: 202.23 seconds
Total tokens generated: 53373
Throughput (tokens/sec): 263.92
Throughput (requests/sec): 0.247
Draft acceptance rate: ~30-50%
## Test 2
Total run time: 196.72 seconds
Total tokens generated: 51990
Throughput (tokens/sec): 264.28
Throughput (requests/sec): 0.254
## Test 3
Total run time: 184.76 seconds
Total tokens generated: 50619
Throughput (tokens/sec): 273.97
Throughput (requests/sec): 0.271

# Quantization (vLLM)
## Test 1
Total run time: 332.04 seconds
Total tokens generated: 59507
Throughput (tokens/sec): 179.21
Throughput (requests/sec): 0.151

# Quantization (Pre-quantized model)
## Test 1
Total run time: 93.02 seconds
Total tokens generated: 57761
Throughput (tokens/sec): 620.93
Throughput (requests/sec): 0.537
## Test 2
Total run time: 89.62 seconds
Total tokens generated: 57929
Throughput (tokens/sec): 646.41
Throughput (requests/sec): 0.558
## Test 3
Total run time: 87.09 seconds
Total tokens generated: 57530
Throughput (tokens/sec): 660.62
Throughput (requests/sec): 0.574

# 1+2+3
## Test 1
Total run time: 53.25 seconds
Total tokens generated: 16390
Throughput (tokens/sec): 307.80
Throughput (requests/sec): 0.939
Draft acceptance rate: ~40-50%
## Test 2
Total run time: 50.96 seconds
Total tokens generated: 16367
Throughput (tokens/sec): 321.18
Throughput (requests/sec): 0.981
## Test 3
Total run time: 48.93 seconds
Total tokens generated: 16222
Throughput (tokens/sec): 331.55
Throughput (requests/sec): 1.022

# 2+3+5
## Test 1
Total run time: 37.12 seconds
Total tokens generated: 20171
Throughput (tokens/sec): 543.46
Throughput (requests/sec): 1.347
Draft acceptance rate: ~30-70%
## Test 2
Total run time: 36.80 seconds
Total tokens generated: 20355
Throughput (tokens/sec): 553.18
Throughput (requests/sec): 1.359
## Test 3
Total run time: 38.51 seconds
Total tokens generated: 20125
Throughput (tokens/sec): 522.52
Throughput (requests/sec): 1.298

# 2+5
## Test 1
Total run time: 22.34 seconds
Total tokens generated: 20272
Throughput (tokens/sec): 907.42
Throughput (requests/sec): 2.238
## Test 2
Total run time: 23.89 seconds
Total tokens generated: 20589
Throughput (tokens/sec): 861.71
Throughput (requests/sec): 2.093
## Test 3
Total run time: 23.9 seconds
Total tokens generated: 20566
Throughput (tokens/sec): 860.87
Throughput (requests/sec): 2.093
