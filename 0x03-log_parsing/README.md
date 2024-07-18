# Log Parsing Project

This project involves reading from standard input (stdin), parsing data in a specific format, and computing metrics based on the input data.

## Concepts Covered

- **File I/O in Python:** Reading from `sys.stdin` line by line.
- **Signal Handling in Python:** Handling keyboard interruptions (CTRL + C) using signal handling in Python.
- **Data Processing:** Parsing strings to extract specific data points, aggregating data to compute summaries.
- **Regular Expressions:** Using regular expressions to validate the format of each line.
- **Dictionaries in Python:** Using dictionaries to count occurrences of status codes and accumulate file sizes.
- **Exception Handling:** Handling possible exceptions during file reading and data processing.

## Components

### 1. Generator Script (`0-generator.py`)

This script generates random log entries in the specified format and writes them to stdout.

### 2. Stats Script (`0-stats.py`)

This script reads from stdin, parses log entries, computes metrics, and prints statistics after every 10 lines or upon receiving a keyboard interruption (CTRL + C).

### Usage

1. **Generate Logs:**

   ```bash
   ./0-generator.py | ./0-stats.py
