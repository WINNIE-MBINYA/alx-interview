# UTF-8 Validation

This project contains a Python function to determine if a given data set represents a valid UTF-8 encoding.

## Files

- `0-validate_utf8.py`: Contains the `validUTF8` function.
- `0-main.py`: Main file for testing the function.

## Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Run the main file to test the function:

    ```bash
    ./0-main.py
    ```

## Function Description

### `validUTF8(data)`

Determines if a given data set represents a valid UTF-8 encoding.

**Arguments:**
- `data` (list of int): A list of integers representing bytes.

**Returns:**
- `bool`: True if data is a valid UTF-8 encoding, else False.

## Example

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))  # True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # True

data = [229, 65, 127, 256]
print(validUTF8(data))  # False
