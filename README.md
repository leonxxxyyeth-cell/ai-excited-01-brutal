# Koi Emas Menembus Lukisan

[![make.fun](https://img.shields.io/badge/make.fun-bounty-gold)](https://make.fun/bounty/ai-excited-01)

Entry for the make.fun bounty **[Make the AI judge excited](https://make.fun/bounty/ai-excited-01)** (`ai-excited-01`).

![Koi Emas Menembus Lukisan](entry.jpg)

## The concept

A giant golden koi smashes out of its ornate golden museum frame — canvas
shredded, liquid gold pouring onto the marble floor, god rays cutting through
the gallery while visitors freeze in awe. A painting that refuses to stay a
painting: the impossible moment, frozen mid-explosion.

Why this image: the winning pattern in this bounty is a creature breaking out
of its frame with gold, scale and drama — awe, wonder and surprise in a single
glance.

## How the program works

`main.py` (Python 3.13, standard library only) copies the bundled image
`entry.jpg` to `/output/entry.png`. It is fully deterministic — run it twice
and the output bytes are identical.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
