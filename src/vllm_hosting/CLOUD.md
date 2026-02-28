Vanilla version

```bash
uv run --active \
    --with vllm \
    vllm serve Qwen/Qwen3-32B \
    --override-generation-config '{"temperature": 0}'
```

With speculative decoding

```bash
uv run --active \
    --with vllm \
    vllm serve Qwen/Qwen3-32B \
    --override-generation-config '{"temperature": 0}' \
    --speculative_config '{"method": "ngram", "model": "Qwen/Qwen3-14B-AWQ", "num_speculative_tokens": 5}'
```

With Quantization (vLLM)

```bash
uv run --active \
    --with vllm \
    vllm serve Qwen/Qwen3-32B \
    --override-generation-config '{"temperature": 0}' \
    --quantization bitsandbytes
```

With Quantization (Pre-quantized model)

```bash
uv run --active \
    --with vllm \
    vllm serve Qwen/Qwen3-32B-AWQ \
    --override-generation-config '{"temperature": 0}'
```

With speculative decoding + Quantization (Pre-quantized model)

```bash
uv run --active \
    --with vllm \
    vllm serve Qwen/Qwen3-32B-AWQ \
    --override-generation-config '{"temperature": 0}' \
    --speculative_config '{"method": "ngram", "model": "Qwen/Qwen3-14B-AWQ", "num_speculative_tokens": 5}'
```
