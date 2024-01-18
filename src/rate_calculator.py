from typing import Dict, List, Tuple, Optional
from operators import Operator


class RateCalculator:
    """Calculates the best rate for a phone number given multiple operators.

    Attributes:
        operators (List[Operator]): A list of telephone operators.

    Methods:
        add_operator(operator): Adds an operator to the calculator.
        bulk_insert_operators(operators_data): Bulk insert operators with their rates.
        find_cheapest_operator(number): Finds the cheapest operator
        for a given number.
    """

    def __init__(self) -> None:
        self.operators = []

    def add_operator(self, operator: Operator) -> None:
        """Adds an operator for the rate calculator."""
        self.operators.append(operator)

    def bulk_insert_operators(self, operators_data: Dict[str, List[Tuple[str, float]]]) -> None:
        """Bulk insert operators with their rates"""
        for operator_name, prefix_rates in operators_data.items():
            operator = Operator(operator_name)
            operator.bulk_insert_prefix_rates(prefix_rates)
            self.add_operator(operator)

    def find_cheapest_operator(self, number: str) -> Tuple[Optional[Operator], Optional[float]]:
        """Finds the cheapest operator for a given phone number.

        Args:
            number (str): The phone number to find the cheapest rate for.

        Returns:
            Tuple[Optional[Operator], Optional[float]]: The cheapest operator
            and its rate, or None if no operator is found.
        """
        cheapest_rate = float('inf')
        cheapest_operator = None
        for operator in self.operators:
            rate = operator.get_rate_for_number(number)
            if rate is not None and rate < cheapest_rate:
                cheapest_rate = rate
                cheapest_operator = operator
        return (cheapest_operator, cheapest_rate if cheapest_operator else None)


if __name__ == '__main__':

    operators_data = {
        "Operator A": [('1', 0.9), ('46', 0.17), ('468', 0.15), ('4620', 0.0),
                       ('4631', 0.15), ('4673', 0.9), ('46732', 1.1), ('268', 5.1)],
        "Operator B": [('1', 0.92), ('44', 0.5), ('46', 0.2), ('467', 1.0), ('48', 1.2)]
    }

    calculator = RateCalculator()
    calculator.bulk_insert_operators(operators_data)

    phone_number = '4673212345'
    cheapest_operator, rate = calculator.find_cheapest_operator(phone_number)

    if cheapest_operator:
        print('Cheapest Operator: {}, Rate: {}'.format(cheapest_operator.name, rate))
    else:
        print('No operator found for this phone number')
