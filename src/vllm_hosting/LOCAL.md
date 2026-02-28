#### Hosting vLLM

There has been some issues when I try to host vLLM using the official docker image.
Therefore, here I provided the uv commands instead.

Vanilla version

```bash
# Here I set max_model_len to 8192 due to memory constraints
uv run --active \
    --with vllm \
    vllm serve Qwen/Qwen3-4B \
    --max_model_len 8192 \
    --override-generation-config '{"temperature": 0}'
```

With speculative decoding

```bash
uv run --active \
    --with vllm \
    vllm serve Qwen/Qwen3-4B \
    --max_model_len 8192 \
    --override-generation-config '{"temperature": 0}' \
    --speculative_config '{"method": "ngram", "model": "Qwen/Qwen3-0.6B", "num_speculative_tokens": 5}'
```

With Quantization (vLLM)

```bash
uv run --active \
    --with vllm \
    vllm serve Qwen/Qwen3-4B \
    --max_model_len 8192 \
    --override-generation-config '{"temperature": 0}' \
    --quantization bitsandbytes
```

With Quantization (Pre-quantized model)

```bash
uv run --active \
    --with vllm \
    vllm serve Qwen/Qwen3-4B-AWQ \
    --max_model_len 8192 \
    --override-generation-config '{"temperature": 0}'
```

With speculative decoding + Quantization (Pre-quantized model)

```bash
uv run --active \
    --with vllm \
    vllm serve Qwen/Qwen3-4B-AWQ \
    --max_model_len 8192 \
    --override-generation-config '{"temperature": 0}' \
    --speculative_config '{"method": "ngram", "model": "Qwen/Qwen3-0.6B", "num_speculative_tokens": 5}'
```
