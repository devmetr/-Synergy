# API Documentation

This document provides comprehensive API documentation for all public functions and components in the project.

## Function Reference

### case1.py

#### `calculate_factorial(n)`

**Purpose**: Calculates the factorial of a given positive integer.

**Function Signature**:
```python
def calculate_factorial(n: int) -> int
```

**Parameters**:
| Parameter | Type | Description | Required | Default |
|-----------|------|-------------|----------|---------|
| `n` | `int` | The positive integer to calculate factorial for | Yes | None |

**Return Value**:
| Type | Description |
|------|-------------|
| `int` | The factorial of the input number |

**Exceptions**:
| Exception | Condition | Message |
|-----------|-----------|---------|
| `ValueError` | When `n` is not a positive integer | "Число должно быть целым положительным числом." |

**Algorithm**: Uses Python's built-in `math.factorial()` function for efficient computation.

**Time Complexity**: O(n) - linear time complexity
**Space Complexity**: O(1) - constant space complexity

**Examples**:

```python
# Basic usage
result = calculate_factorial(5)
print(result)  # Output: 120

# Edge case: factorial of 0
result = calculate_factorial(0)
print(result)  # Output: 1

# Error handling
try:
    result = calculate_factorial(-5)
except ValueError as e:
    print(e)  # Output: Число должно быть целым положительным числом.

# Type validation
try:
    result = calculate_factorial("5")
except ValueError as e:
    print(e)  # Output: Число должно быть целым положительным числом.
```

**Input Validation**:
- Ensures input is an integer using `isinstance(n, int)`
- Ensures input is non-negative using `n < 0`
- Provides clear error messages in Russian

**Mathematical Properties**:
- `factorial(0) = 1` (by definition)
- `factorial(1) = 1`
- `factorial(n) = n × (n-1) × (n-2) × ... × 2 × 1`

### case2.py

#### `игра_угадай_число()`

**Purpose**: Runs an interactive number guessing game.

**Function Signature**:
```python
def игра_угадай_число() -> None
```

**Parameters**: None

**Return Value**: None (void function)

**Game Mechanics**:
- **Range**: Numbers from 1 to 100 (inclusive)
- **Attempts**: 7 attempts maximum
- **Feedback**: Provides hints after each guess
- **Win Condition**: Correct number guessed within attempts
- **Lose Condition**: All attempts exhausted

**Game Flow**:
1. Generates random number using `random.randint(1, 100)`
2. Displays welcome message and rules
3. Enters main game loop (7 iterations)
4. Processes user input for each attempt
5. Provides feedback (too high/too low/correct)
6. Handles invalid input gracefully
7. Displays final result

**Input Handling**:
- Accepts integer input from user
- Validates input type using `int(input())`
- Handles `ValueError` for non-integer input
- Continues game after invalid input

**User Interface Messages**:
```python
# Welcome message
"Добро пожаловать в игру 'Угадай число'!"
"Я загадал число от 1 до 100. У вас есть 7 попыток, чтобы угадать его."

# Game prompts
f"Попытка {попытка}: Введите ваше предположение: "

# Feedback messages
"Слишком маленькое число!"
"Слишком большое число!"
f"Поздравляю! Вы угадали число за {попытка} попыток!"

# Error messages
"Ошибка! Введите целое число."

# Game over message
f"К сожалению, у вас закончились попытки. Загаданное число было {загаданное_число}."
```

**Examples**:

```python
# Start the game
from case2 import игра_угадай_число

игра_угадай_число()
```

**Sample Game Session**:
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

**Error Handling**:
- **Invalid Input**: Catches `ValueError` and continues game
- **Graceful Recovery**: Maintains attempt count after invalid input
- **User-Friendly Messages**: Clear instructions and feedback

**Random Number Generation**:
- Uses `random.randint(1, 100)` for fair number distribution
- Each game generates a new random number
- Range is inclusive of both 1 and 100

## Module-Level Information

### case1.py Module

**Dependencies**:
- `math` - Standard library module for mathematical functions

**Public Interface**:
- `calculate_factorial(n)` - Main public function

**Private Components**:
- Main execution block with interactive input handling
- Error handling for user input validation

**Usage Patterns**:
- **Direct Execution**: Run as script for interactive factorial calculation
- **Import Usage**: Import function for use in other modules
- **Library Function**: Use as mathematical utility in larger applications

### case2.py Module

**Dependencies**:
- `random` - Standard library module for random number generation

**Public Interface**:
- `игра_угадай_число()` - Main public function

**Private Components**:
- Game logic and state management
- User input processing
- Game flow control

**Usage Patterns**:
- **Direct Execution**: Run as script for interactive gameplay
- **Import Usage**: Import function for integration into larger applications
- **Educational Tool**: Demonstrate user input handling and game logic

## Integration Examples

### Combining Both Modules

```python
from case1 import calculate_factorial
from case2 import игра_угадай_число

def math_game_session():
    """Combines factorial calculation with number guessing game."""
    print("Welcome to Math Game Session!")
    
    # Calculate some factorials
    numbers = [5, 6, 7]
    for num in numbers:
        result = calculate_factorial(num)
        print(f"Factorial of {num} is {result}")
    
    print("\nNow let's play the number guessing game!")
    игра_угадай_число()

# Run the combined session
math_game_session()
```

### Error Handling Integration

```python
from case1 import calculate_factorial

def robust_factorial_calculator():
    """Demonstrates comprehensive error handling."""
    test_inputs = [5, -1, "abc", 3.14, 0, 100]
    
    for input_val in test_inputs:
        try:
            result = calculate_factorial(input_val)
            print(f"✓ Factorial of {input_val} = {result}")
        except ValueError as e:
            print(f"✗ ValueError for {input_val}: {e}")
        except Exception as e:
            print(f"✗ Unexpected error for {input_val}: {e}")

robust_factorial_calculator()
```

## Performance Characteristics

### case1.py Performance

- **Time Complexity**: O(n) - linear growth with input size
- **Space Complexity**: O(1) - constant memory usage
- **Input Limits**: Limited by Python's `math.factorial()` implementation
- **Memory Usage**: Minimal, only stores the result

### case2.py Performance

- **Time Complexity**: O(1) - constant time per game
- **Space Complexity**: O(1) - constant memory usage
- **Game Duration**: Variable based on user input speed
- **Memory Usage**: Minimal, only stores game state variables

## Best Practices

### Using case1.py

1. **Input Validation**: Always validate input before calling the function
2. **Error Handling**: Use try-catch blocks for robust error handling
3. **Performance**: For large numbers, consider the computational cost
4. **Type Safety**: Ensure input is an integer before calling

### Using case2.py

1. **User Experience**: Provide clear instructions to users
2. **Input Validation**: Handle invalid input gracefully
3. **Game Balance**: Consider adjusting attempt limits for different skill levels
4. **Accessibility**: Ensure error messages are clear and helpful

## Testing Recommendations

### Unit Tests for case1.py

```python
import unittest
from case1 import calculate_factorial

class TestCalculateFactorial(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(calculate_factorial(0), 1)
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(5), 120)
    
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate_factorial(-1)
        with self.assertRaises(ValueError):
            calculate_factorial("5")

if __name__ == '__main__':
    unittest.main()
```

### Integration Tests

```python
def test_module_integration():
    """Test that both modules can be imported and used together."""
    try:
        from case1 import calculate_factorial
        from case2 import игра_угадай_число
        
        # Test factorial function
        result = calculate_factorial(5)
        assert result == 120, f"Expected 120, got {result}"
        
        print("✓ All modules imported successfully")
        print("✓ Factorial function working correctly")
        print("✓ Ready for game function testing")
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

test_module_integration()
```