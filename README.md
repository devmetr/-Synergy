# Python Project Documentation

This project contains two main Python modules with utility functions and interactive programs.

## Table of Contents

- [Installation](#installation)
- [Modules](#modules)
  - [case1.py](#case1py)
  - [case2.py](#case2py)
- [API Reference](#api-reference)
- [Usage Examples](#usage-examples)
- [Error Handling](#error-handling)
- [Requirements](#requirements)

## Installation

No additional dependencies are required beyond Python's standard library.

```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Run the modules directly
python case1.py
python case2.py
```

## Modules

### case1.py

A factorial calculator module that provides mathematical computation functionality.

**File Purpose**: Mathematical utility for calculating factorials with input validation.

**Main Function**: `calculate_factorial(n)`

### case2.py

An interactive number guessing game module.

**File Purpose**: Interactive game that demonstrates user input handling and game logic.

**Main Function**: `игра_угадай_число()`

## API Reference

### case1.py

#### `calculate_factorial(n)`

Calculates the factorial of a given positive integer using the math library.

**Signature**: `def calculate_factorial(n: int) -> int`

**Parameters**:
- `n` (int): A positive integer to calculate factorial for

**Returns**:
- `int`: The factorial of the input number

**Raises**:
- `ValueError`: If `n` is not a positive integer

**Example**:
```python
from case1 import calculate_factorial

# Calculate factorial of 5
result = calculate_factorial(5)  # Returns 120

# Calculate factorial of 0
result = calculate_factorial(0)  # Returns 1

# This will raise ValueError
try:
    result = calculate_factorial(-1)
except ValueError as e:
    print(e)  # "Число должно быть целым положительным числом."
```

### case2.py

#### `игра_угадай_число()`

Runs an interactive number guessing game where the player tries to guess a randomly generated number.

**Signature**: `def игра_угадай_число() -> None`

**Parameters**: None

**Returns**: None

**Game Rules**:
- The game generates a random number between 1 and 100
- Player has 7 attempts to guess the number
- After each guess, the game provides feedback (too high/too low)
- Game ends when the number is guessed or attempts are exhausted

**Example**:
```python
from case2 import игра_угадай_число

# Start the game
игра_угадай_число()
```

## Usage Examples

### Example 1: Using the Factorial Calculator

```python
# Import the function
from case1 import calculate_factorial

# Calculate various factorials
print(calculate_factorial(5))    # Output: 120
print(calculate_factorial(10))   # Output: 3628800
print(calculate_factorial(0))    # Output: 1

# Handle invalid input
try:
    calculate_factorial(-5)
except ValueError as e:
    print(f"Error: {e}")
```

### Example 2: Running the Number Guessing Game

```python
# Import and run the game
from case2 import игра_угадай_число

# Start the game (interactive)
игра_угадай_число()
```

**Game Flow Example**:
```
Добро пожаловать в игру 'Угадай число'!
Я загадал число от 1 до 100. У вас есть 7 попыток, чтобы угадать его.
Попытка 1: Введите ваше предположение: 50
Слишком большое число!
Попытка 2: Введите ваше предположение: 25
Слишком маленькое число!
Попытка 3: Введите ваше предположение: 37
Поздравляю! Вы угадали число за 3 попыток!
```

### Example 3: Error Handling

```python
from case1 import calculate_factorial

# Handle various error cases
test_cases = [5, -1, "abc", 3.14, 0]

for test_case in test_cases:
    try:
        result = calculate_factorial(test_case)
        print(f"Factorial of {test_case} is {result}")
    except ValueError as e:
        print(f"Cannot calculate factorial of {test_case}: {e}")
    except TypeError as e:
        print(f"Type error for {test_case}: {e}")
```

## Error Handling

### case1.py Error Handling

The `calculate_factorial` function includes comprehensive error handling:

- **Type Validation**: Ensures input is an integer
- **Range Validation**: Ensures input is non-negative
- **Clear Error Messages**: Provides descriptive error messages in Russian

### case2.py Error Handling

The number guessing game handles:

- **Input Validation**: Ensures user input is a valid integer
- **Graceful Error Recovery**: Continues the game after invalid input
- **User-Friendly Messages**: Clear feedback for all game states

## Requirements

- **Python Version**: 3.6 or higher
- **Standard Library Modules**:
  - `math` (for factorial calculations)
  - `random` (for number generation)
  - `builtins` (for input/output operations)

## Running the Project

### Interactive Mode

```bash
# Run the factorial calculator
python case1.py

# Run the number guessing game
python case2.py
```

### Import Mode

```python
# Import and use functions in your own code
from case1 import calculate_factorial
from case2 import игра_угадай_число

# Use the functions
result = calculate_factorial(6)
игра_угадай_число()
```

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues, please open an issue in the project repository.