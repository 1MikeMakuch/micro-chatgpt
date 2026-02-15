# MicroGPT-C
The most atomic way to train and inference a GPT in pure, dependency-free C.

## Compilation and Running

Compile with optimizations:

```bash
gcc -O3 -march=native -ffast-math -o gpt gpt.c -lm
```

**Flags explained:**
- `-O3`: Maximum optimization
- `-march=native`: Use CPU-specific instructions (AVX, etc.)
- `-ffast-math`: Faster floating point (trades some precision)
- `-lm`: Link math library (for sqrt, exp, etc.)

Run:

```bash
./gpt
```

You should see loss decreasing, then generated samples!
