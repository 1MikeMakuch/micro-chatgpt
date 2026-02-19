# Micro-ChatGPT
The smallest GPT that can hold a human-like conversation, in pure C. Fored from [microgpt-c](https://github.com/vixhal-baraiya/microgpt-c).

## Usage

```bash
make            # gcc -O3 -march=native -ffast-math -o micro-chatgpt micro-chatgpt.c -lm
make train      # ./micro-chatgpt --data chat.txt --steps 30000 (1 or 2 mins)

./micro-chatgpt --load model.bin --temperature 0.5

```

## Options

| Flag | Default | Description |
|------|---------|-------------|
| `--load FILE` | none | Load saved model, skip training |
| `--save FILE` | `model.bin` | Save model after training |
| `--data FILE` | `chat.txt` | Training data file |
| `--steps N` | 30000 | Training steps |
| `--temperature F` | 0.5 | Sampling temperature |

In interactive mode, type a prompt and press Enter. Type `quit` to exit.
