from nodes.trie import TrieNode
from base_rate_calculator import BaseRateCalculator
from typing import List, Tuple, Optional


class Operator(BaseRateCalculator):
    """Represents a telephone operator with a pricing trie.

    Attributes:
        name (str): The name of the operator.
        trie_root (TrieNode): The root node of the trie.

    Methods:
        bulk_insert_prefix_rates(prefix_rates): Inserts multiple prefixes
        and their rates.
        insert_prefix_rate(prefix, rate): Inserts a single prefix
        and its rate.
        get_rate_for_number(number): Retrieves the rate for
        a given phone number.
    """

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.trie_root: TrieNode = TrieNode()

    def bulk_insert_prefix_rates(self, prefix_rates: List[Tuple[str, float]]) -> None:
        """Bulk inserts multiple prefixes and
        their rates to the trie."""

        for prefix, rate in prefix_rates:
            self.insert_prefix_rate(prefix, rate)

    def insert_prefix_rate(self, prefix: str, rate: float) -> None:
        """Insert a single prefix and its rate to the trie."""

        curr_node = self.trie_root
        for digit in prefix:
            if digit not in curr_node.children:
                curr_node.children[digit] = TrieNode()
            curr_node = curr_node.children[digit]
        curr_node.rate = rate

    def get_rate_for_number(self, number: str) -> Optional[float]:
        """Retrieves the rate for a given number using the longest matching prefix.

        Args:
            number (str): The phone number to find the rate for.

        Returns:
            Optional[float]: The rate for the given number or None if no rate is found.
        """
        curr_node = self.trie_root
        last_rate = None
        for digit in number:
            if digit in curr_node.children:
                curr_node = curr_node.children[digit]
                if curr_node.rate is not None:
                    last_rate = curr_node.rate
            else:
                break
        return last_rate