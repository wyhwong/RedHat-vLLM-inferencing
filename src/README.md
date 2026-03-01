# Demo code for vLLM Inferencing

This README is a brief introduction to the code repository. It contains the following sections:
- [Installation: Dependencies for This Repository](#installation-dependencies-for-this-repository)
- [Demonstration: Setup for Ollama Hosting](#demonstration-setup-for-ollama-hosting)
- [Demonstration: Setup for vLLM Hosting](#demonstration-setup-for-vllm-hosting)
- [Demonstration: Descriptions of Notebooks](#demonstration-descriptions-of-notebooks)

## Installation: Dependencies for This Repository

```bash
# If you haven't installed uv
pipx install uv

uv sync --active
uv pip install vllm==0.15.0 --torch-backend=auto
```

## Demonstration: Setup for Ollama Hosting

Please see [README.md](./src/ollama_hosting/README.md) for hosting a Qwen3 4B model with Ollama.

## Demonstration: Setup for vLLM Hosting

Please see [LOCAL.md](./src/vllm_hosting/LOCAL.md) for hosting a Qwen3 4B model with vLLM.

If you have enough hardware resources, you may also see [CLOUD.md](./src/vllm_hosting/CLOUD.md) for hosting a Qwen3 32B model with vLLM.

If you want to reproduce the results in [speculative decoding blog](https://blog.vllm.ai/2024/10/17/spec-decode.html), you may check out [BLOG_REPRODUCTION.md](./src/vllm_hosting/BLOG_REPRODUCTION.md) for hosting OPT-6.7B with vLLM.

## Demonstration: Descriptions of Notebooks

- ### [0. Simple Inference with vLLM](./notebooks/0_simple_inference_with_vllm.ipynb)

    This notebook contains the least amount of code to run inference with vLLM. It serves as a quick start guide for users who never used vLLM or any LLM serving system with OpenAI API compatible interface before.

- ### [1. Prepare Inference Prompts from Alpaca](./notebooks/1_prepare_inference_prompts_from_alpaca.ipynb)

    This notebook shows how to prepare inference prompts used in the talk from the Alpaca dataset.

- ### [2. Inference with Ollama](./notebooks/2_inference_with_ollama.ipynb)

    This notebook shows the steps to run inference with Ollama, and also contains the simple metrics to evaluate performance of Ollama inference.

- ### [3. Inference with vLLM](./notebooks/3_inference_with_vllm.ipynb)

    This notebook shows the steps to run inference with vLLM, and also contains the simple metrics to evaluate performance of vLLM inference.

- ### [4. Visualize Hardware Metrics](./notebooks/4_visualize_hardware_metrics.ipynb)

    This notebook shows the visualization of GPU utilization and memory usage during inference with Ollama and vLLM, which is used to support explanation the performance difference between the two systems.
