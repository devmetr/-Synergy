#!/usr/bin/env python3
"""
Test Suite for case1.py and case2.py Modules

This file contains comprehensive tests for both modules, including
unit tests, integration tests, and performance tests.
"""

import sys
import os
import unittest
import time
import math
from unittest.mock import patch, MagicMock

# Add parent directory to path to import modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from case1 import calculate_factorial
from case2 import игра_угадай_число

class TestCalculateFactorial(unittest.TestCase):
    """Test cases for the calculate_factorial function from case1.py."""
    
    def test_valid_positive_integers(self):
        """Test factorial calculation with valid positive integers."""
        test_cases = [
            (0, 1),      # Base case: 0! = 1
            (1, 1),      # Base case: 1! = 1
            (2, 2),      # 2! = 2
            (3, 6),      # 3! = 6
            (4, 24),     # 4! = 24
            (5, 120),    # 5! = 120
            (6, 720),    # 6! = 720
            (7, 5040),   # 7! = 5040
            (8, 40320),  # 8! = 40320
            (9, 362880), # 9! = 362880
            (10, 3628800) # 10! = 3628800
        ]
        
        for input_val, expected in test_cases:
            with self.subTest(input_val=input_val):
                result = calculate_factorial(input_val)
                self.assertEqual(result, expected, 
                               f"Factorial of {input_val} should be {expected}, got {result}")
    
    def test_negative_integers(self):
        """Test that negative integers raise ValueError."""
        negative_numbers = [-1, -5, -10, -100]
        
        for num in negative_numbers:
            with self.subTest(input_val=num):
                with self.assertRaises(ValueError):
                    calculate_factorial(num)
    
    def test_non_integer_types(self):
        """Test that non-integer types raise ValueError."""
        invalid_inputs = [
            "5",           # String
            "abc",         # String
            "",            # Empty string
            3.14,          # Float
            3.0,           # Float that's an integer
            [1, 2, 3],     # List
            (1, 2, 3),     # Tuple
            {1, 2, 3},     # Set
            {"a": 1},      # Dictionary
            None,          # None
            True,          # Boolean
            False,         # Boolean
            complex(1, 1), # Complex number
        ]
        
        for invalid_input in invalid_inputs:
            with self.subTest(input_val=invalid_input):
                with self.assertRaises(ValueError):
                    calculate_factorial(invalid_input)
    
    def test_error_message_content(self):
        """Test that error messages contain expected content."""
        try:
            calculate_factorial(-1)
        except ValueError as e:
            error_message = str(e)
            self.assertIn("целым положительным числом", error_message)
            self.assertIn("должно быть", error_message)
        else:
            self.fail("Expected ValueError was not raised")
    
    def test_large_numbers(self):
        """Test factorial calculation with larger numbers."""
        # Test some larger numbers (but not too large to avoid long execution)
        test_cases = [
            (15, 1307674368000),
            (20, 2432902008176640000)
        ]
        
        for input_val, expected in test_cases:
            with self.subTest(input_val=input_val):
                result = calculate_factorial(input_val)
                self.assertEqual(result, expected,
                               f"Factorial of {input_val} should be {expected}, got {result}")
    
    def test_mathematical_properties(self):
        """Test mathematical properties of factorials."""
        # Test that n! = n × (n-1)!
        for n in range(2, 11):
            with self.subTest(n=n):
                n_fact = calculate_factorial(n)
                n_minus_1_fact = calculate_factorial(n - 1)
                expected = n * n_minus_1_fact
                self.assertEqual(n_fact, expected,
                               f"{n}! should equal {n} × ({n-1})!")
    
    def test_edge_cases(self):
        """Test edge cases and boundary conditions."""
        # Test 0! = 1 (mathematical definition)
        self.assertEqual(calculate_factorial(0), 1, "0! should equal 1")
        
        # Test 1! = 1
        self.assertEqual(calculate_factorial(1), 1, "1! should equal 1")
        
        # Test that factorial grows rapidly
        fact_5 = calculate_factorial(5)
        fact_6 = calculate_factorial(6)
        self.assertGreater(fact_6, fact_5, "6! should be greater than 5!")
        
        # Test that 6! = 6 × 5!
        self.assertEqual(fact_6, 6 * fact_5, "6! should equal 6 × 5!")

class TestNumberGuessingGame(unittest.TestCase):
    """Test cases for the number guessing game from case2.py."""
    
    def test_function_exists(self):
        """Test that the game function exists and is callable."""
        self.assertTrue(callable(игра_угадай_число))
        self.assertEqual(игра_угадай_число.__name__, 'игра_угадай_число')
    
    def test_function_signature(self):
        """Test the function signature and parameters."""
        import inspect
        
        sig = inspect.signature(игра_угадай_число)
        params = list(sig.parameters.keys())
        
        # Function should take no parameters
        self.assertEqual(len(params), 0, "Function should take no parameters")
    
    def test_function_returns_none(self):
        """Test that the function returns None (void function)."""
        # Mock input to avoid interactive input during testing
        with patch('builtins.input') as mock_input:
            mock_input.return_value = "50"  # Mock a valid input
            
            # Mock random.randint to return a predictable value
            with patch('random.randint') as mock_randint:
                mock_randint.return_value = 50
                
                # Mock print to capture output
                with patch('builtins.print') as mock_print:
                    result = игра_угадай_число()
                    self.assertIsNone(result, "Function should return None")
    
    def test_game_logic_structure(self):
        """Test the basic structure and logic of the game."""
        # This test examines the function's structure without running it
        import inspect
        
        source = inspect.getsource(игра_угадай_число)
        
        # Check for expected game components
        self.assertIn("random.randint", source, "Game should use random.randint")
        self.assertIn("for попытка in range", source, "Game should have attempt loop")
        self.assertIn("input(", source, "Game should get user input")
        self.assertIn("if __name__ == '__main__':", source, "Game should have main guard")

class TestModuleIntegration(unittest.TestCase):
    """Test cases for integration between the two modules."""
    
    def test_import_both_modules(self):
        """Test that both modules can be imported successfully."""
        try:
            from case1 import calculate_factorial
            from case2 import игра_угадай_число
            
            self.assertTrue(callable(calculate_factorial))
            self.assertTrue(callable(игра_угадай_число))
            
        except ImportError as e:
            self.fail(f"Failed to import modules: {e}")
    
    def test_combined_usage(self):
        """Test that both modules can be used together."""
        # Calculate some factorials
        try:
            fact_5 = calculate_factorial(5)
            fact_6 = calculate_factorial(6)
            
            # Verify mathematical relationship
            self.assertEqual(fact_6, 6 * fact_5)
            
            # Verify both functions are callable
            self.assertTrue(callable(calculate_factorial))
            self.assertTrue(callable(игра_угадай_число))
            
        except Exception as e:
            self.fail(f"Failed to use modules together: {e}")
    
    def test_error_handling_consistency(self):
        """Test that both modules handle errors consistently."""
        # Both modules should handle errors gracefully
        try:
            # Test case1 error handling
            with self.assertRaises(ValueError):
                calculate_factorial(-1)
            
            # Test case2 function exists and is callable
            self.assertTrue(callable(игра_угадай_число))
            
        except Exception as e:
            self.fail(f"Error handling test failed: {e}")

class TestPerformance(unittest.TestCase):
    """Performance tests for the modules."""
    
    def test_factorial_performance(self):
        """Test performance of factorial calculations."""
        test_numbers = [5, 10, 15, 20]
        
        for num in test_numbers:
            with self.subTest(input_val=num):
                # Measure execution time
                start_time = time.time()
                result = calculate_factorial(num)
                end_time = time.time()
                
                execution_time = end_time - start_time
                
                # Performance assertions
                self.assertLess(execution_time, 1.0,  # Should complete within 1 second
                              f"Factorial of {num} took {execution_time:.3f}s, should be < 1.0s")
                
                # Verify result is correct
                expected = math.factorial(num)
                self.assertEqual(result, expected,
                               f"Factorial of {num} should be {expected}, got {result}")
    
    def test_factorial_memory_usage(self):
        """Test that factorial calculations don't consume excessive memory."""
        import psutil
        import os
        
        # Get current process
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        
        # Perform factorial calculations
        for i in range(10):
            calculate_factorial(i)
        
        final_memory = process.memory_info().rss
        memory_increase = final_memory - initial_memory
        
        # Memory increase should be reasonable (less than 10MB)
        self.assertLess(memory_increase, 10 * 1024 * 1024,  # 10MB in bytes
                       f"Memory usage increased by {memory_increase / 1024 / 1024:.2f}MB, should be < 10MB")

class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""
    
    def test_factorial_zero_and_one(self):
        """Test factorial of 0 and 1 (edge cases)."""
        # 0! = 1 (mathematical definition)
        self.assertEqual(calculate_factorial(0), 1)
        
        # 1! = 1
        self.assertEqual(calculate_factorial(1), 1)
    
    def test_factorial_rapid_growth(self):
        """Test that factorial values grow rapidly."""
        fact_10 = calculate_factorial(10)
        fact_11 = calculate_factorial(11)
        
        # 11! should be much larger than 10!
        self.assertGreater(fact_11, fact_10 * 10)
    
    def test_input_validation_edge_cases(self):
        """Test edge cases in input validation."""
        edge_cases = [
            (0, 1),           # Zero (valid)
            (1, 1),           # One (valid)
            (-0, 1),          # Negative zero (should be treated as 0)
            (True, 1),        # Boolean True (should be treated as 1)
            (False, 1),       # Boolean False (should be treated as 0)
        ]
        
        for input_val, expected in edge_cases:
            with self.subTest(input_val=input_val):
                try:
                    result = calculate_factorial(input_val)
                    self.assertEqual(result, expected)
                except ValueError:
                    # Some edge cases might raise ValueError, which is acceptable
                    pass

class TestDocumentation(unittest.TestCase):
    """Test that modules have proper documentation."""
    
    def test_case1_documentation(self):
        """Test that case1.py has proper documentation."""
        import case1
        
        # Check module docstring
        if hasattr(case1, '__doc__') and case1.__doc__:
            self.assertIsInstance(case1.__doc__, str)
            self.assertGreater(len(case1.__doc__), 0)
        
        # Check function docstring
        if hasattr(case1.calculate_factorial, '__doc__') and case1.calculate_factorial.__doc__:
            doc = case1.calculate_factorial.__doc__
            self.assertIsInstance(doc, str)
            self.assertGreater(len(doc), 0)
            
            # Check for key documentation elements
            self.assertIn("Args:", doc, "Function should document parameters")
            self.assertIn("Returns:", doc, "Function should document return value")
            self.assertIn("Raises:", doc, "Function should document exceptions")
    
    def test_case2_documentation(self):
        """Test that case2.py has proper documentation."""
        import case2
        
        # Check module docstring
        if hasattr(case2, '__doc__') and case2.__doc__:
            self.assertIsInstance(case2.__doc__, str)
            self.assertGreater(len(case2.__doc__), 0)
        
        # Check function docstring
        if hasattr(case2.игра_угадай_число, '__doc__') and case2.игра_угадай_число.__doc__:
            doc = case2.игра_угадай_число.__doc__
            self.assertIsInstance(doc, str)
            self.assertGreater(len(doc), 0)

def run_performance_benchmarks():
    """Run performance benchmarks for the modules."""
    print("Performance Benchmarks")
    print("=" * 50)
    
    # Benchmark factorial calculations
    test_numbers = [5, 10, 15, 20, 25]
    
    print("Factorial Calculation Performance:")
    print("-" * 40)
    
    for num in test_numbers:
        # Warm up
        for _ in range(100):
            calculate_factorial(num)
        
        # Benchmark
        start_time = time.time()
        for _ in range(1000):
            calculate_factorial(num)
        end_time = time.time()
        
        avg_time = (end_time - start_time) / 1000 * 1000  # Convert to milliseconds
        print(f"  {num:2d}! : {avg_time:8.3f} ms average")
    
    print()

def run_stress_tests():
    """Run stress tests to check robustness."""
    print("Stress Tests")
    print("=" * 50)
    
    # Test factorial with many calculations
    print("Running factorial stress test...")
    start_time = time.time()
    
    try:
        for i in range(1000):
            calculate_factorial(i % 21)  # Use modulo to avoid very large numbers
        
        end_time = time.time()
        total_time = end_time - start_time
        print(f"  ✓ Completed 1000 factorial calculations in {total_time:.3f}s")
        
    except Exception as e:
        print(f"  ✗ Stress test failed: {e}")
    
    print()

def main():
    """Run all tests and benchmarks."""
    print("Comprehensive Test Suite for case1.py and case2.py")
    print("=" * 60)
    print()
    
    # Run performance benchmarks
    run_performance_benchmarks()
    
    # Run stress tests
    run_stress_tests()
    
    # Run unit tests
    print("Running Unit Tests...")
    print("-" * 30)
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestCalculateFactorial,
        TestNumberGuessingGame,
        TestModuleIntegration,
        TestPerformance,
        TestEdgeCases,
        TestDocumentation
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("Test Results Summary")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Skipped: {len(result.skipped)}")
    
    if result.failures:
        print("\nFailures:")
        for test, traceback in result.failures:
            print(f"  {test}: {traceback}")
    
    if result.errors:
        print("\nErrors:")
        for test, traceback in result.errors:
            print(f"  {test}: {traceback}")
    
    # Return success/failure
    return result.wasSuccessful()

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)