# Prime Game

## Description

The **Prime Game** project involves implementing a Python function to determine the winner of a game played by Maria and Ben. The game is played with a set of consecutive integers starting from 1 up to and including `n`. The players take turns choosing a prime number from the set, and each turn, the chosen prime number and its multiples are removed from the set. The player who cannot make a move loses the game.

This project includes:
- Implementing the prime number calculation using the Sieve of Eratosthenes.
- Simulating multiple rounds of the game to determine the overall winner.
- Adhering to PEP 8 style guidelines and ensuring all code files are executable.

## Requirements

- All code will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
- All code files must end with a new line.
- The first line of all code files must be exactly `#!/usr/bin/python3`.
- A `README.md` file, located at the root of the project directory, is mandatory.
- The code must use the PEP 8 style guide (version 1.7.x).
- All code files must be executable.

## Usage

### Function Prototype

```python
def isWinner(x, nums):
