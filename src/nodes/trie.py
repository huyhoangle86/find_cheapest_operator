

class TrieNode:
    """A node in the Trie structure for storing telephone number
        prefixes and rates.

    Attributes:
        children (Dict[str, 'TrieNode']): A dictionary mapping a digit
        to the next TrieNode.
        rate (Optional[float]): The rate associated with the prefix
        at this node.
    """

    def __init__(self) -> None:
        self.children = {}
        self.rate = None
