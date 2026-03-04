## From Offline to Online Inference: Why Serving Is Hard—and How vLLM Helps

This repository demonstrates the usage of vLLM, designed to support the talk "From Offline to Online Inference: Why Serving Is Hard—and How vLLM Helps" at vLLM Hong Kong Meetup, March 2026. The goal is to showcase how performance differences between vLLM and Ollama, alos to provide a reference for further acceleration techniques such as speculative decoding.

<div align="center">

[![RedHat](https://img.shields.io/badge/RedHat-E8004F)](https://www.redhat.com/)
[![HKPUG](https://img.shields.io/badge/HKPUG-green)](https://python.hk/)
[![OSHK](https://img.shields.io/badge/OSHK-00AEEF)](https://opensource.hk/)
[![PolyU](https://img.shields.io/badge/PolyU-E4405F)](https://www.polyu.edu.hk/)

![vLLM Meetup](./assets/vLLM-HK-Meetup_banner.png)

</div>

## Usage

```bash
git clone https://github.com/wyhwong/RedHat-vLLM-inferencing.git
cd RedHat-vLLM-inferencing
```

See [README.md](./src/README.md) for more details.

## Abstract of Talk

As large language models (LLMs) transition from research prototypes to production systems, inference becomes a primary bottleneck, and the gap between “it runs” and “it serves” widens quickly. While offline inference can be optimized for throughput, online inference must handle concurrency, variable-length prompts, and unpredictable workloads, making strong performance much harder to achieve.

In this talk, we begin with a quick introduction to LLM inference, then contrast offline and online settings, highlighting why online serving is challenging. We then compare Ollama and vLLM on a small benchmark of 50 requests sampled from the Alpaca dataset, showing how vLLM can achieve significantly faster runtime. We also explain the core features behind vLLM: PagedAttention and continuous batching, and relate them to hardware behavior such as GPU utilization and memory usage. Finally, we briefly explore additional techniques to accelerate inference in practice, such as prompt engineering and speculative decoding.

## Related Resources

- Powerpoint Slides: [View on OneDrive](https://1drv.ms/p/c/7adfdf652c41fb6c/IQCQLBuD6L5SQp-1BF9-yh2eAcN2yYvzUR9KphCrrzNmEK4)

- Talk Homepage: [vLLM Hong Kong Meetup](https://www.vantagemind.com/events/vLLM/260307/vLLM-HK-Meetup_Session-Abstracts.html#abs-offline-to-online)

For the slides, you may also find them in [slides_backup](./slides_backup) directory.

## Acknowledgement

Thanks [Alex Au](https://github.com/alex-au-922) for sponsoring the testing on Runpod using NVIDIA B200 GPU.

## Author
[@wyhwong](https://github.com/wyhwong)
