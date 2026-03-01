#### Hosting Ollama with Docker

## Designated Setup

| Item                         | Value                          |
| ---------------------------- | ------------------------------ |
| Target model                 | Qwen/Qwen3-4B                  |
| Target model (Pre-quantized) | Qwen/Qwen3-4B-AWQ              |
| Draft model                  | Qwen/Qwen3-0.6B                |
| GPU                          | NVIDIA RTX 4060 Ti (16GB VRAM) |

## OLLAMA_NUM_PARALLEL=4

```bash
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -e MODEL_NAME="qwen3:4b" \
  -e OLLAMA_CONTEXT_LENGTH="8192" \
  -e OLLAMA_NUM_PARALLEL=4 \
  --runtime nvidia --gpus all \
  --entrypoint sh \
  ollama/ollama:0.15.4 \
  -lc '
    set -e
    echo "Starting Ollama..."
    ollama serve &
    sleep 5
    ollama run "${MODEL_NAME}"
    tail -f /dev/null
  '
```

## OLLAMA_NUM_PARALLEL=8

```bash
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -e MODEL_NAME="qwen3:4b" \
  -e OLLAMA_CONTEXT_LENGTH="8192" \
  -e OLLAMA_NUM_PARALLEL=8 \
  --runtime nvidia --gpus all \
  --entrypoint sh \
  ollama/ollama:0.15.4 \
  -lc '
    set -e
    echo "Starting Ollama..."
    ollama serve &
    sleep 5
    ollama run "${MODEL_NAME}"
    tail -f /dev/null
  '
```

## OLLAMA_NUM_PARALLEL=12

```bash
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -e MODEL_NAME="qwen3:4b" \
  -e OLLAMA_CONTEXT_LENGTH="8192" \
  -e OLLAMA_NUM_PARALLEL=12 \
  --runtime nvidia --gpus all \
  --entrypoint sh \
  ollama/ollama:0.15.4 \
  -lc '
    set -e
    echo "Starting Ollama..."
    ollama serve &
    sleep 5
    ollama run "${MODEL_NAME}"
    tail -f /dev/null
  '
```
