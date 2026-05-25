# AGENTS.md

## Cursor Cloud specific instructions

### Overview

This repository contains two standalone Python CLI scripts that use only the Python standard library (`math`, `random`). No external dependencies, build tools, or services are required.

| File | Description |
|---|---|
| `case1.py` | Interactive factorial calculator — prompts for a positive integer, prints its factorial |
| `case2.py` | "Guess the Number" game — random number 1–100, 7 attempts |

### Running

```bash
python3 case1.py   # Interactive: enter a number, get its factorial
python3 case2.py   # Interactive: guess the hidden number
```

### Testing

Both scripts are interactive (`input()`). To test non-interactively, pipe input:

```bash
echo "5" | python3 case1.py          # Factorial of 5
printf '50\n25\n75\n' | python3 case2.py  # Multiple guesses
```

Syntax check:

```bash
python3 -m py_compile case1.py
python3 -m py_compile case2.py
```

### Caveats

- `case1.py` has top-level interactive code (a `while True` loop), so importing it directly (`from case1 import ...`) will block on `input()`. Test its `calculate_factorial` function by redefining it or piping input.
- `case2.py` is guarded by `if __name__ == "__main__"`, so it can be imported safely.
- No linter, formatter, or test framework is configured in the repo.
