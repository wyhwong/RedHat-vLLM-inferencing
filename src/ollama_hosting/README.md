#### Hosting Ollama with Docker

```bash
docker run -d \
  --name ollama \
  -p 11434:11434 \
  -e MODEL_NAME="qwen3:4b" \
  -e OLLAMA_CONTEXT_LENGTH="8192" \
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
