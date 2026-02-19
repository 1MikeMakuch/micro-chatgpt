CC = gcc
CFLAGS = -O3 -march=native -ffast-math
LDFLAGS = -lm

micro-chatgpt: micro-chatgpt.c
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS)

train: micro-chatgpt
	./micro-chatgpt --data chat.txt --steps 30000
	@echo ""
	@echo "Run: ./micro-chatgpt --load model.bin --temperature 0.5"

clean:
	rm -f micro-chatgpt model.bin

.PHONY: clean train
