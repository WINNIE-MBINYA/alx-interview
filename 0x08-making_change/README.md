# 0x08. Making Change

## Description

This project tackles the classic problem from dynamic programming and greedy algorithms: the coin change problem. The objective is to determine the minimum number of coins required to meet a given total amount, given a list of coin denominations.

## Learning Objectives

### Key Concepts:

- **Greedy Algorithms:**
  - Understanding how greedy algorithms operate and their suitability for the coin change problem.
  - Recognizing scenarios where greedy algorithms might not provide the optimal solution.

- **Dynamic Programming:**
  - Applying the principles of dynamic programming to solve optimization problems.
  - Understanding overlapping subproblems and optimal substructure in the context of the coin change problem.

- **Algorithmic Complexity:**
  - Analyzing the time and space complexity of different algorithms.
  - Striving for efficient solutions with lower complexity to meet runtime constraints.

- **Problem-Solving Strategies:**
  - Breaking down the problem into smaller, manageable sub-problems.
  - Exploring iterative vs. recursive approaches in dynamic programming.

- **Python Programming:**
  - Manipulating lists and using list comprehensions effectively.
  - Implementing functions with efficient looping and conditional statements.

## Project Requirements

- **Environment:**
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
  - Code should comply with PEP 8 style (version 1.7.x).
  - All files must be executable.

- **File Structure:**
  - A `README.md` file at the root of the project directory is mandatory.
  - The first line of all Python files should be `#!/usr/bin/python3`.
  - All files should end with a new line.

## Task

### 0. Change comes from within

- **Objective:**
  - Given a pile of coins of different values, determine the fewest number of coins needed to meet a given total.

- **Prototype:**
  ```python
  def makeChange(coins, total):
      """Determine the minimum number of coins required to meet total."""
