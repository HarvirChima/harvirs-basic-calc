#!/usr/bin/env python3
"""
Unit Tests for Basic Calculator

Run tests with: python test_basic_calc.py
"""

import unittest
from basic_calc import BasicCalculator


class TestBasicCalculator(unittest.TestCase):
    """Test cases for the BasicCalculator class."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = BasicCalculator()
    
    def test_addition_positive_numbers(self):
        """Test addition with positive numbers."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        self.assertEqual(self.calc.add(0, 5), 5)
    
    def test_addition_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-10, 5), -5)
    
    def test_addition_decimal_numbers(self):
        """Test addition with decimal numbers."""
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertEqual(self.calc.add(0.1, 0.2), 0.30000000000000004)  # Floating point precision
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=10)
    
    def test_addition_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, -3), -3)
    
    def test_subtraction_positive_numbers(self):
        """Test subtraction with positive numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(1, 1), 0)
    
    def test_subtraction_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-3, -5), 2)
        self.assertEqual(self.calc.subtract(5, -3), 8)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
    
    def test_subtraction_decimal_numbers(self):
        """Test subtraction with decimal numbers."""
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=10)
    
    def test_subtraction_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
    
    def test_history_tracking(self):
        """Test calculation history functionality."""
        # Initially empty
        self.assertEqual(len(self.calc.get_history()), 0)
        
        # Add some calculations
        self.calc.add(2, 3)
        self.calc.subtract(10, 4)
        
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("2 + 3 = 5", history[0])
        self.assertIn("10 - 4 = 6", history[1])
    
    def test_clear_history(self):
        """Test clearing calculation history."""
        # Add some calculations
        self.calc.add(1, 1)
        self.calc.subtract(5, 2)
        
        # Verify history has items
        self.assertEqual(len(self.calc.get_history()), 2)
        
        # Clear history
        self.calc.clear_history()
        
        # Verify history is empty
        self.assertEqual(len(self.calc.get_history()), 0)
    
    def test_large_numbers(self):
        """Test calculations with large numbers."""
        large_num = 1000000
        self.assertEqual(self.calc.add(large_num, 1), 1000001)
        self.assertEqual(self.calc.subtract(large_num, 1), 999999)
    
    def test_small_numbers(self):
        """Test calculations with very small numbers."""
        small_num = 0.000001
        result = self.calc.add(small_num, small_num)
        self.assertAlmostEqual(result, 0.000002, places=6)
        
        result = self.calc.subtract(small_num, small_num)
        self.assertAlmostEqual(result, 0.0, places=6)


class TestBasicCalculatorIntegration(unittest.TestCase):
    """Integration tests for basic calculator operations."""
    
    def setUp(self):
        self.calc = BasicCalculator()
    
    def test_sequential_operations(self):
        """Test performing multiple operations in sequence."""
        # Start with 10
        result1 = self.calc.add(5, 5)  # 10
        result2 = self.calc.subtract(result1, 3)  # 7
        result3 = self.calc.add(result2, 8)  # 15
        result4 = self.calc.subtract(result3, 5)  # 10
        
        self.assertEqual(result1, 10)
        self.assertEqual(result2, 7)
        self.assertEqual(result3, 15)
        self.assertEqual(result4, 10)
        
        # Check that all operations are in history
        history = self.calc.get_history()
        self.assertEqual(len(history), 4)
    
    def test_alternating_operations(self):
        """Test alternating between addition and subtraction."""
        results = []
        
        # Perform alternating operations
        results.append(self.calc.add(0, 5))      # 5
        results.append(self.calc.subtract(10, 3)) # 7
        results.append(self.calc.add(2, 8))      # 10
        results.append(self.calc.subtract(15, 5)) # 10
        
        expected = [5, 7, 10, 10]
        self.assertEqual(results, expected)


def run_performance_tests():
    """Run basic performance tests."""
    import time
    
    calc = BasicCalculator()
    
    # Test performance with many operations
    start_time = time.time()
    for i in range(1000):
        calc.add(i, i + 1)
        calc.subtract(i + 2, i)
    end_time = time.time()
    
    print(f"\nPerformance Test Results:")
    print(f"2,000 operations completed in {end_time - start_time:.4f} seconds")
    print(f"Average time per operation: {(end_time - start_time) / 2000 * 1000:.6f} ms")
    
    # Test memory usage
    history_size = len(calc.get_history())
    print(f"History contains {history_size} operations")


if __name__ == '__main__':
    # Run unit tests
    print("Running Basic Calculator Unit Tests...")
    print("=" * 45)
    
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test classes
    test_suite.addTest(unittest.makeSuite(TestBasicCalculator))
    test_suite.addTest(unittest.makeSuite(TestBasicCalculatorIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    # Run performance tests
    run_performance_tests()
    
    # Print summary
    print("\n" + "=" * 45)
    if result.wasSuccessful():
        print("🎉 All tests passed!")
    else:
        print(f"❌ {len(result.failures)} test(s) failed, {len(result.errors)} error(s)")
        
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
