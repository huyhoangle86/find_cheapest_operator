import os
import sys
import unittest
from typing import Dict, List, Tuple
sys.path.append(os.path.abspath(os.curdir))

from rate_calculator import Operator, RateCalculator


class TestRateCalculator(unittest.TestCase):

    def test_insert_prefix_rate(self):
        """Instert prefix and rate pair one by one"""
        operator = Operator('Unittest Operator')
        operator.insert_prefix_rate('232', 0.5)
        self.assertEqual(operator.get_rate_for_number('232'), 0.5)
        self.assertIsNone(operator.get_rate_for_number('456'))

    def test_bulk_insert_prefix_rates(self):
        """Bulk instert prefix and rate pairs"""
        operator = Operator('Unittest Operator')
        rates = [('096', 0.1), ('234', 0.2)]
        operator.bulk_insert_prefix_rates(rates)
        self.assertEqual(operator.get_rate_for_number('096'), 0.1)
        self.assertEqual(operator.get_rate_for_number('234'), 0.2)

    def test_find_cheapest_operator(self):
        """Given phone number, find cheapest operator"""
        operators_data = {
            "Operator A": [('123', 0.8)],
            "Operator B": [('123', 0.92)]    
        }
        rate_calculator = RateCalculator()
        rate_calculator.bulk_insert_operators(operators_data)
        cheapest_operator, rate = rate_calculator.find_cheapest_operator("123")
        self.assertIsNotNone(cheapest_operator)
        self.assertEqual(cheapest_operator.name, 'Operator A')
        self.assertEqual(rate, 0.8)

    def test_no_operator_found(self):
        """
        Return None if there aren't any operator
        found for input phone number
        """
        operators_data = {
            "Operator A": [('123', 0.8)],
            "Operator B": [('123', 0.92)]
        }
        rate_calculator = RateCalculator()
        rate_calculator.bulk_insert_operators(operators_data)
        cheapest_operator, rate = rate_calculator.find_cheapest_operator('234')
        self.assertIsNone(cheapest_operator)
        self.assertIsNone(rate)

    def generate_large_dataset(self, num_entries: int) -> Dict[str, List[Tuple[str, float]]]:
        """Generate a large dataset of prefix-rate pairs."""
        operators_data = {}
        for i in range(1, num_entries + 1):
            operator_name = f"Operator {i}"
            prefix_rate = [("1" * (i % 10), float(i) / 100)]
            operators_data[operator_name] = prefix_rate
        return operators_data

    def test_with_large_dataset(self):
        """
        Generate large dataset and bulk insert
        then test to query a number
        """
        operators_data = self.generate_large_dataset(1000)
        calculator = RateCalculator()
        calculator.bulk_insert_operators(operators_data)

        # add a test to query a number  
        number = '1111111111'
        cheapest_operator, rate = calculator.find_cheapest_operator(number)

        # Asserts to ensure that the program returns valid values
        self.assertIsNotNone(cheapest_operator)
        self.assertIsInstance(rate, float)


if __name__ == '__main__':
    unittest.main()
