# Hosting vLLM for Inference (Local)

## Designated Setup

| Item                         | Value                          |
| ---------------------------- | ------------------------------ |
| Target model                 | facebook/opt-6.7b              |
| Draft model                  | facebook/opt-125m              |
| GPU                          | NVIDIA RTX 4060 Ti (16GB VRAM) |

## Note

This README is for reproducing the results in [How Speculative Decoding Boosts vLLM Performance by up to 2.8x, 2024](https://blog.vllm.ai/2024/10/17/spec-decode.html
).

## Vanilla version

```bash
uv run --active \
    --with vllm \
    vllm serve facebook/opt-6.7b \
    --override-generation-config '{"temperature": 0}' \
    --chat-template ./vllm_hosting/template_chat.jinja
```

## With speculative decoding

```bash
uv run --active \
    --with vllm \
    vllm serve facebook/opt-6.7b \
    --override-generation-config '{"temperature": 0}' \
    --speculative_config '{"method": "ngram", "model": "facebook/opt-125m", "num_speculative_tokens": 5}' \
    --chat-template ./vllm_hosting/template_chat.jinja
```
