"""
Unit Tests for Temperature Sensor Program
This file contains unit tests for the temperature_sensor.py module,
covering boundary value analysis, robustness testing, and special scenarios.
"""

import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.temperature_sensor import process_temperatures, format_output, find_min, find_max, calculate_average


class TestTemperatureSensor(unittest.TestCase):
    """Test cases for the Temperature Sensor program"""

    def test_case_1a_single_value(self):
        """Test Case 1A: Single value input [20]"""
        result = process_temperatures([20])
        self.assertEqual(result["min"], 20)
        self.assertEqual(result["max"], 20)
        self.assertEqual(result["avg"], 20)
        self.assertEqual(format_output(result), "Min: 20°C, Max: 20°C, Avg: 20°C")

    def test_case_1b_two_values(self):
        """Test Case 1B: Two values input [15, 35]"""
        result = process_temperatures([15, 35])
        self.assertEqual(result["min"], 15)
        self.assertEqual(result["max"], 35)
        self.assertEqual(result["avg"], 25)
        self.assertEqual(format_output(result), "Min: 15°C, Max: 35°C, Avg: 25°C")

    def test_case_2a_empty_list(self):
        """Test Case 2A: Empty list input []"""
        result = process_temperatures([])
        self.assertIn("error", result)
        self.assertEqual(result["error"], "No input provided.")
        self.assertEqual(format_output(result), "No input provided.")

    def test_case_3a_mixed_values(self):
        """Test Case 3A: Mixed values input [10, -10, 30]"""
        result = process_temperatures([10, -10, 30])
        self.assertEqual(result["min"], -10)
        self.assertEqual(result["max"], 30)
        self.assertEqual(result["avg"], 10)
        self.assertEqual(format_output(result), "Min: -10°C, Max: 30°C, Avg: 10°C")

    def test_case_4a_boundary_values(self):
        """Test Case 4A: Boundary values input [-50, 20, 150, 25]"""
        result = process_temperatures([-50, 20, 150, 25])
        self.assertEqual(result["min"], -50)
        self.assertEqual(result["max"], 150)
        self.assertEqual(result["avg"], 36.25)
        self.assertEqual(format_output(result), "Min: -50°C, Max: 150°C, Avg: 36.25°C")

    def test_case_4b_invalid_input(self):
        """Test Case 4B: Invalid input [10, "abc", 30]"""
        result = process_temperatures([10, "abc", 30])
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Invalid input detected.")
        self.assertEqual(format_output(result), "Invalid input detected.")

    def test_minimum_boundary(self):
        """Test minimum boundary input [-50]"""
        result = process_temperatures([-50])
        self.assertEqual(result["min"], -50)
        self.assertEqual(result["max"], -50)
        self.assertEqual(result["avg"], -50)

    def test_maximum_boundary(self):
        """Test maximum boundary input [150]"""
        result = process_temperatures([150])
        self.assertEqual(result["min"], 150)
        self.assertEqual(result["max"], 150)
        self.assertEqual(result["avg"], 150)

    def test_near_boundary_values(self):
        """Test near-boundary values input [-49, 149]"""
        result = process_temperatures([-49, 149])
        self.assertEqual(result["min"], -49)
        self.assertEqual(result["max"], 149)
        self.assertEqual(result["avg"], 50)

    def test_mixed_valid_invalid_values(self):
        """Test mixed valid and invalid inputs [-60, 20, 160]"""
        result = process_temperatures([-60, 20, 160])
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Out-of-bound value detected.")

    def test_special_characters(self):
        """Test special characters in input [10, '@', -40]"""
        result = process_temperatures([10, "@", -40])
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Invalid input detected.")

    def test_very_large_input(self):
        """Test very large input values [2**31 - 1, -2**31]"""
        result = process_temperatures([2**31 - 1, -2**31])
        self.assertIn("error", result)
        self.assertEqual(result["error"], "Out-of-bound value detected.")

    def test_all_same_values(self):
        """Test all inputs are the same [50, 50, 50]"""
        result = process_temperatures([50, 50, 50])
        self.assertEqual(result["min"], 50)
        self.assertEqual(result["max"], 50)
        self.assertEqual(result["avg"], 50)
        
    def test_find_min_empty_list(self):
        """Test find_min with empty list"""
        result = find_min([])
        self.assertIsNone(result)
        
    def test_find_max_empty_list(self):
        """Test find_max with empty list"""
        result = find_max([])
        self.assertIsNone(result)
        
    def test_calculate_average_empty_list(self):
        """Test calculate_average with empty list"""
        result = calculate_average([])
        self.assertIsNone(result)
        
    def test_multiple_identical_values(self):
        """Test with multiple identical values [25, 25, 25, 25]"""
        result = process_temperatures([25, 25, 25, 25])
        self.assertEqual(result["min"], 25)
        self.assertEqual(result["max"], 25)
        self.assertEqual(result["avg"], 25)
        
    def test_negative_values_only(self):
        """Test with only negative values [-30, -20, -10]"""
        result = process_temperatures([-30, -20, -10])
        self.assertEqual(result["min"], -30)
        self.assertEqual(result["max"], -10)
        self.assertEqual(result["avg"], -20)


if __name__ == "__main__":
    unittest.main()