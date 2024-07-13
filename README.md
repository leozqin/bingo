# Bingo
`bingo` is a framework for using composable version-controlled human-and-machine readable configurations to dynamically generate verifiably-random stochastically-distributed rulesets for highly-personalized extended-reality weakly-scoped prize-drive metagames of heterogenous domain on commodity hardware using memory-safe, privacy-aware, standards-compliant technologies.

If that's too much of a mouthful, you can also call it a bingo card generator.

One particular that is nice about it, though, is that you provide your configuration as `yml` files, so you can store them and have access to them later on. The full set of `YAML 1.1` conventions is supported.

# Configuration Schema
```yml
# The title of the card, used for generating file names
title: Road Trip Bingo
# The number of variants to produce. Each one will be independently randomized
variants: 3
# The size of the card - must be an odd number. The resulting card is <size> x <size> square.
size: 5
# <optional> the fixed center piece (traditionally the "free" space) of the card - will be the same for all variants
center: Wearing seatbelts
# an array containing the items that should be randomized into the variants, as below. Must be at least <size>**2 (including center when counting)
items:
- A funny hat
- A license plate from Wyoming
- ...
```

# Install
Python version 3.10 or greater is required to use `bingo`.

## Recommended: Install using pipx
1. Install [pipx](https://github.com/pypa/pipx)
2. Install bingo using pipx: `pipx install git+https://github.com/leozqin/bingo.git`

## Alternatively: Install using pip
1. Create a fresh virtualenv using `python -m venv .venv`
2. Activate that virtualenv: `.venv/bin/activate`
3. Install bingo using pip: `pip install git+https://github.com/leozqin/bingo.git`

## Usage
Use the `bingo` CLI tool to generate bingo cards. It only takes a single argument, which is the path where the config file is stored.

```bash
bingo ./path/to/config.yml
```

The output is a `pdf` file created in your `pwd` that contains all of your configured variants - `Road Trip Bingo.pdf` for the example above.