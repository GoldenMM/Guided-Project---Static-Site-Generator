import unittest
from main import split_nodes_delimiter
from textnode import TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_no_delimiter(self):
        old_nodes = [TextNode("Hello, World!", "text")]
        new_nodes = split_nodes_delimiter(old_nodes, "*", "bold")
        self.assertEqual(new_nodes, old_nodes)

    def test_split_nodes_delimiter_with_delimiter(self):
        old_nodes = [TextNode("Hello, *World*!", "text")]
        new_nodes = split_nodes_delimiter(old_nodes, "*", "bold")
        expected_nodes = [TextNode("Hello, ", "text"), TextNode("World", "bold"), TextNode("!", "text")]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_invalid_syntax(self):
        old_nodes = [TextNode("Hello, *World!", "text")]
        with self.assertRaises(Exception):
            split_nodes_delimiter(old_nodes, "*", "bold")

    def test_split_nodes_delimiter_non_text_node(self):
        old_nodes = [TextNode("Hello, World!", "image")]
        new_nodes = split_nodes_delimiter(old_nodes, "*", "bold")
        self.assertEqual(new_nodes, old_nodes)

if __name__ == "__main__":
    unittest.main()