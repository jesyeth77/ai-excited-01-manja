# Paus Emas Menembus Jendela Kaca Patri

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/ai-excited-01)

Entry for the make.fun bounty [Make the AI judge excited](https://make.fun/bounty/ai-excited-01).

## The concept

A colossal golden whale leaps straight through the rose window of a Gothic
cathedral, shattering the stained glass into a burst of glowing golden
shards. Impossible scale, a frozen moment of pure momentum, and light
exploding everywhere at once — the kind of image that hits you before you
have time to think about it.

## How it works

`main.py` is a one-line deterministic program: it copies the bundled
`entry.jpg` byte for byte to `/output/entry.png`. No timestamps, no
randomness, no network — two runs produce identical bytes.

Run it locally:

```sh
mkdir -p /tmp/out && MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `main.py` — the entry program (copies `entry.jpg` to `/output/entry.png`)
- `entry.jpg` — the entry image (1024×1024 JPEG, 332,283 bytes)
- `LICENSE` — MIT
