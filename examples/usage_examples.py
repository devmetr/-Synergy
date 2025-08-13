#!/usr/bin/env python3
"""
Usage Examples for case1.py and case2.py Modules

This file demonstrates various ways to use the factorial calculator and
number guessing game modules, including integration examples and advanced usage patterns.
"""

import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from case1 import calculate_factorial
from case2 import игра_угадай_число

def example_1_basic_factorial_usage():
    """Example 1: Basic factorial calculation usage."""
    print("=" * 50)
    print("Example 1: Basic Factorial Usage")
    print("=" * 50)
    
    # Calculate factorials for common numbers
    test_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for num in test_numbers:
        try:
            result = calculate_factorial(num)
            print(f"Factorial of {num:2d} = {result:>10d}")
        except ValueError as e:
            print(f"Error calculating factorial of {num}: {e}")
    
    print()

def example_2_factorial_error_handling():
    """Example 2: Comprehensive error handling for factorial function."""
    print("=" * 50)
    print("Example 2: Factorial Error Handling")
    print("=" * 50)
    
    # Test various invalid inputs
    invalid_inputs = [
        (-5, "Negative number"),
        (-1, "Negative one"),
        ("abc", "String input"),
        (3.14, "Float input"),
        ([1, 2, 3], "List input"),
        (None, "None input"),
        (True, "Boolean input"),
        (False, "Boolean input"),
        ("", "Empty string"),
        ("123", "String number")
    ]
    
    for test_input, description in invalid_inputs:
        print(f"Testing: {description} ({test_input})")
        try:
            result = calculate_factorial(test_input)
            print(f"  ✓ Result: {result}")
        except ValueError as e:
            print(f"  ✗ ValueError: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected error: {type(e).__name__}: {e}")
    
    print()

def example_3_factorial_batch_processing():
    """Example 3: Batch processing of factorial calculations."""
    print("=" * 50)
    print("Example 3: Batch Factorial Processing")
    print("=" * 50)
    
    # Process a range of numbers
    start_num = 0
    end_num = 15
    
    results = {}
    errors = []
    
    for num in range(start_num, end_num + 1):
        try:
            result = calculate_factorial(num)
            results[num] = result
            print(f"✓ {num:2d}! = {result:>15d}")
        except ValueError as e:
            errors.append((num, str(e)))
            print(f"✗ {num:2d}! = Error: {e}")
    
    # Summary
    print(f"\nSummary:")
    print(f"  Successful calculations: {len(results)}")
    print(f"  Errors: {len(errors)}")
    print(f"  Range: {start_num} to {end_num}")
    
    if errors:
        print(f"  Error details:")
        for num, error in errors:
            print(f"    {num}: {error}")
    
    print()

def example_4_factorial_mathematical_analysis():
    """Example 4: Mathematical analysis using factorial results."""
    print("=" * 50)
    print("Example 4: Mathematical Analysis")
    print("=" * 50)
    
    import math
    
    # Calculate factorials and related mathematical values
    numbers = [5, 6, 7, 8, 9, 10]
    
    print("Number | Factorial | Square Root | Natural Log | Log10")
    print("-" * 60)
    
    for num in numbers:
        try:
            factorial = calculate_factorial(num)
            sqrt_fact = math.sqrt(factorial)
            ln_fact = math.log(factorial)
            log10_fact = math.log10(factorial)
            
            print(f"{num:6d} | {factorial:9d} | {sqrt_fact:11.2f} | {ln_fact:11.2f} | {log10_fact:6.2f}")
        except ValueError as e:
            print(f"{num:6d} | Error: {e}")
    
    print()

def example_5_factorial_calculator_class():
    """Example 5: Creating a calculator class using the factorial function."""
    print("=" * 50)
    print("Example 5: Factorial Calculator Class")
    print("=" * 50)
    
    class FactorialCalculator:
        def __init__(self):
            self.history = []
            self.cache = {}
        
        def calculate(self, n):
            """Calculate factorial with caching and history."""
            # Check cache first
            if n in self.cache:
                self.history.append(f"factorial({n}) = {self.cache[n]} (cached)")
                return self.cache[n]
            
            try:
                result = calculate_factorial(n)
                self.cache[n] = result
                self.history.append(f"factorial({n}) = {result}")
                return result
            except ValueError as e:
                self.history.append(f"Error calculating factorial({n}): {e}")
                raise
        
        def get_history(self):
            """Return calculation history."""
            return self.history
        
        def get_cache(self):
            """Return current cache."""
            return self.cache
        
        def clear_history(self):
            """Clear calculation history."""
            self.history = []
        
        def clear_cache(self):
            """Clear calculation cache."""
            self.cache = {}
    
    # Usage example
    calc = FactorialCalculator()
    
    # Calculate some factorials
    test_numbers = [5, 6, 7, 5, 6]  # Note: 5 and 6 repeated for caching
    
    for num in test_numbers:
        try:
            result = calc.calculate(num)
            print(f"Calculated: {num}! = {result}")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Show history and cache
    print(f"\nCalculation History:")
    for entry in calc.get_history():
        print(f"  {entry}")
    
    print(f"\nCache Contents:")
    for num, result in calc.get_cache().items():
        print(f"  {num}! = {result}")
    
    print()

def example_6_number_game_integration():
    """Example 6: Integration between factorial calculator and number game."""
    print("=" * 50)
    print("Example 6: Module Integration")
    print("=" * 50)
    
    def math_game_session():
        """Combines mathematical calculations with number guessing."""
        print("Welcome to Math Game Session!")
        print("Let's start with some mathematical calculations...")
        
        # Calculate some interesting factorials
        interesting_numbers = [5, 6, 7, 8]
        print("\nCalculating factorials:")
        
        for num in interesting_numbers:
            try:
                result = calculate_factorial(num)
                print(f"  {num}! = {result}")
            except ValueError as e:
                print(f"  Error calculating {num}!: {e}")
        
        # Show some mathematical relationships
        print("\nMathematical relationships:")
        try:
            fact_5 = calculate_factorial(5)
            fact_6 = calculate_factorial(6)
            fact_7 = calculate_factorial(7)
            
            print(f"  6! = 6 × 5! = 6 × {fact_5} = {fact_6}")
            print(f"  7! = 7 × 6! = 7 × {fact_6} = {fact_7}")
            
        except ValueError as e:
            print(f"  Error in calculations: {e}")
        
        print("\nNow let's play the number guessing game!")
        print("(Note: This will start an interactive game session)")
        print("(You can play the game or press Ctrl+C to skip)")
        
        try:
            # Uncomment the next line to actually play the game
            # игра_угадай_число()
            print("Game function call commented out for demonstration")
        except KeyboardInterrupt:
            print("\nGame skipped.")
        except Exception as e:
            print(f"Game error: {e}")
    
    # Run the integrated session
    math_game_session()
    print()

def example_7_advanced_factorial_features():
    """Example 7: Advanced features and optimizations for factorial calculations."""
    print("=" * 50)
    print("Example 7: Advanced Factorial Features")
    print("=" * 50)
    
    import time
    import functools
    
    # Performance measurement
    def measure_performance(func, *args, iterations=1000):
        """Measure execution time of a function."""
        start_time = time.time()
        for _ in range(iterations):
            func(*args)
        end_time = time.time()
        return (end_time - start_time) / iterations
    
    # Cached factorial function
    @functools.lru_cache(maxsize=128)
    def cached_factorial(n):
        """Cached version of factorial calculation."""
        return calculate_factorial(n)
    
    # Batch factorial calculator
    def batch_factorial(numbers):
        """Calculate factorials for multiple numbers efficiently."""
        results = {}
        errors = []
        
        for num in numbers:
            try:
                result = cached_factorial(num)
                results[num] = result
            except ValueError as e:
                errors.append((num, str(e)))
        
        return results, errors
    
    # Test performance
    test_numbers = [5, 10, 15, 20]
    
    print("Performance Analysis:")
    print("-" * 30)
    
    for num in test_numbers:
        try:
            # Measure regular factorial
            regular_time = measure_performance(calculate_factorial, num, iterations=1000)
            
            # Measure cached factorial (first call)
            cached_time = measure_performance(cached_factorial, num, iterations=1000)
            
            # Measure cached factorial (subsequent calls)
            cached_time_subsequent = measure_performance(cached_factorial, num, iterations=10000)
            
            print(f"n = {num:2d}:")
            print(f"  Regular:    {regular_time*1000:8.3f} ms")
            print(f"  Cached:     {cached_time*1000:8.3f} ms")
            print(f"  Subsequent: {cached_time_subsequent*1000:8.3f} ms")
            
        except ValueError as e:
            print(f"n = {num:2d}: Error - {e}")
    
    # Test batch processing
    print(f"\nBatch Processing Test:")
    large_range = list(range(0, 21))
    results, errors = batch_factorial(large_range)
    
    print(f"  Numbers processed: {len(large_range)}")
    print(f"  Successful: {len(results)}")
    print(f"  Errors: {len(errors)}")
    
    # Show some results
    print(f"\nSample results:")
    for num in [0, 5, 10, 15, 20]:
        if num in results:
            print(f"  {num:2d}! = {results[num]}")
    
    print()

def example_8_error_handling_patterns():
    """Example 8: Different error handling patterns and strategies."""
    print("=" * 50)
    print("Example 8: Error Handling Patterns")
    print("=" * 50)
    
    def robust_factorial_calculator(inputs):
        """Demonstrates different error handling strategies."""
        results = {
            'successful': [],
            'value_errors': [],
            'type_errors': [],
            'unexpected': []
        }
        
        for input_val in inputs:
            try:
                result = calculate_factorial(input_val)
                results['successful'].append((input_val, result))
                
            except ValueError as e:
                results['value_errors'].append((input_val, str(e)))
                
            except TypeError as e:
                results['type_errors'].append((input_val, str(e)))
                
            except Exception as e:
                results['unexpected'].append((input_val, type(e).__name__, str(e)))
        
        return results
    
    # Test various input types
    test_inputs = [
        5,           # Valid integer
        0,           # Valid edge case
        -5,          # Negative number (ValueError)
        "abc",       # String (ValueError)
        3.14,        # Float (ValueError)
        [1, 2, 3],   # List (ValueError)
        None,        # None (ValueError)
        True,        # Boolean (ValueError)
        False,       # Boolean (ValueError)
        "",          # Empty string (ValueError)
        "123",       # String number (ValueError)
        100,         # Large valid number
    ]
    
    # Process inputs
    results = robust_factorial_calculator(test_inputs)
    
    # Display results by category
    print("Error Handling Results:")
    print("-" * 30)
    
    print(f"Successful calculations ({len(results['successful'])}):")
    for input_val, result in results['successful']:
        print(f"  ✓ {input_val} → {result}")
    
    print(f"\nValueError cases ({len(results['value_errors'])}):")
    for input_val, error in results['value_errors']:
        print(f"  ✗ {input_val}: {error}")
    
    print(f"\nTypeError cases ({len(results['type_errors'])}):")
    for input_val, error in results['type_errors']:
        print(f"  ✗ {input_val}: {error}")
    
    print(f"\nUnexpected errors ({len(results['unexpected'])}):")
    for input_val, error_type, error_msg in results['unexpected']:
        print(f"  ✗ {input_val}: {error_type}: {error_msg}")
    
    print()

def example_9_educational_demonstrations():
    """Example 9: Educational demonstrations and learning examples."""
    print("=" * 50)
    print("Example 9: Educational Demonstrations")
    print("=" * 50)
    
    def factorial_patterns():
        """Demonstrate mathematical patterns in factorials."""
        print("Mathematical Patterns in Factorials:")
        print("-" * 40)
        
        numbers = list(range(0, 11))
        
        print("n  | n!     | Pattern")
        print("-" * 25)
        
        for i, num in enumerate(numbers):
            try:
                result = calculate_factorial(num)
                
                # Identify patterns
                if num == 0 or num == 1:
                    pattern = "Base case"
                elif num > 1:
                    prev_fact = calculate_factorial(num - 1)
                    pattern = f"n × (n-1)! = {num} × {prev_fact}"
                else:
                    pattern = "Invalid"
                
                print(f"{num:2d} | {result:6d} | {pattern}")
                
            except ValueError as e:
                print(f"{num:2d} | Error  | {e}")
    
    def factorial_growth():
        """Demonstrate the rapid growth of factorial values."""
        print(f"\nFactorial Growth Analysis:")
        print("-" * 40)
        
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
        print("n  | n!      | Digits | Growth Factor")
        print("-" * 45)
        
        prev_result = 1
        for num in numbers:
            try:
                result = calculate_factorial(num)
                digits = len(str(result))
                
                if num > 0:
                    growth_factor = result / prev_result
                    growth_str = f"{growth_factor:6.1f}x"
                else:
                    growth_str = "N/A"
                
                print(f"{num:2d} | {result:7d} | {digits:6d} | {growth_str}")
                prev_result = result
                
            except ValueError as e:
                print(f"{num:2d} | Error   | N/A   | N/A")
    
    # Run educational demonstrations
    factorial_patterns()
    factorial_growth()
    print()

def example_10_real_world_applications():
    """Example 10: Real-world applications and use cases."""
    print("=" * 50)
    print("Example 10: Real-World Applications")
    print("=" * 50)
    
    def combination_calculator(n, r):
        """Calculate combinations using factorial."""
        try:
            if r > n or r < 0:
                return 0
            
            n_fact = calculate_factorial(n)
            r_fact = calculate_factorial(r)
            n_r_fact = calculate_factorial(n - r)
            
            return n_fact // (r_fact * n_r_fact)
        except ValueError as e:
            print(f"Error calculating combination: {e}")
            return None
    
    def permutation_calculator(n, r):
        """Calculate permutations using factorial."""
        try:
            if r > n or r < 0:
                return 0
            
            n_fact = calculate_factorial(n)
            n_r_fact = calculate_factorial(n - r)
            
            return n_fact // n_r_fact
        except ValueError as e:
            print(f"Error calculating permutation: {e}")
            return None
    
    def probability_examples():
        """Demonstrate probability calculations using factorials."""
        print("Probability Calculations:")
        print("-" * 30)
        
        # Example 1: Rolling 6 dice, getting all different numbers
        n = 6
        r = 6
        total_outcomes = 6**6
        favorable_outcomes = permutation_calculator(6, 6)
        probability = favorable_outcomes / total_outcomes
        
        print(f"Rolling 6 dice, all different numbers:")
        print(f"  Total outcomes: {6**6:,}")
        print(f"  Favorable outcomes: {favorable_outcomes:,}")
        print(f"  Probability: {probability:.6f} ({probability*100:.4f}%)")
        
        # Example 2: Drawing 5 cards from a deck
        n = 52
        r = 5
        total_combinations = combination_calculator(n, r)
        
        print(f"\nDrawing 5 cards from a 52-card deck:")
        print(f"  Total combinations: {total_combinations:,}")
        
        # Probability of getting 4 aces and 1 king
        aces_combinations = combination_calculator(4, 4)  # Choose all 4 aces
        kings_combinations = combination_calculator(4, 1)  # Choose 1 king
        favorable = aces_combinations * kings_combinations
        probability = favorable / total_combinations
        
        print(f"  Probability of 4 aces + 1 king: {probability:.10f}")
    
    def statistical_analysis():
        """Demonstrate statistical applications."""
        print(f"\nStatistical Applications:")
        print("-" * 30)
        
        # Stirling's approximation for large factorials
        print("Stirling's Approximation (n! ≈ √(2πn) × (n/e)ⁿ):")
        
        import math
        
        for n in [5, 10, 20]:
            try:
                exact = calculate_factorial(n)
                stirling = math.sqrt(2 * math.pi * n) * (n / math.e) ** n
                error = abs(exact - stirling) / exact * 100
                
                print(f"  n = {n:2d}:")
                print(f"    Exact:     {exact:,}")
                print(f"    Stirling:   {stirling:,.0f}")
                print(f"    Error:      {error:.2f}%")
                
            except ValueError as e:
                print(f"  n = {n:2d}: Error - {e}")
    
    # Run real-world examples
    probability_examples()
    statistical_analysis()
    print()

def main():
    """Run all examples."""
    print("Comprehensive Usage Examples for case1.py and case2.py")
    print("=" * 70)
    print()
    
    # Run all examples
    examples = [
        example_1_basic_factorial_usage,
        example_2_factorial_error_handling,
        example_3_factorial_batch_processing,
        example_4_factorial_mathematical_analysis,
        example_5_factorial_calculator_class,
        example_6_number_game_integration,
        example_7_advanced_factorial_features,
        example_8_error_handling_patterns,
        example_9_educational_demonstrations,
        example_10_real_world_applications
    ]
    
    for i, example_func in enumerate(examples, 1):
        try:
            example_func()
        except Exception as e:
            print(f"Error running example {i}: {e}")
            print()
    
    print("=" * 70)
    print("All examples completed!")
    print("\nTo run individual examples, call the specific function:")
    print("  example_1_basic_factorial_usage()")
    print("  example_2_factorial_error_handling()")
    print("  # ... etc.")

if __name__ == "__main__":
    main()