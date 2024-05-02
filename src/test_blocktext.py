# FILEPATH: /home/xerxes/Documents/Boot.dev/Guided Project - Static Site Generator/src/test_blocktext.py

import unittest
from blocktext import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_line(self):
        text = "Hello, World!"
        expected = ["Hello, World!"]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_multiple_lines(self):
        text = "Hello,\nWorld!"
        expected = ["Hello,", "World!"]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_leading_trailing_whitespace(self):
        text = "  Hello, World!  "
        expected = ["Hello, World!"]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_empty_lines(self):
        text = "\n\nHello,\n\nWorld!\n\n"
        expected = ["", "", "Hello,", "", "World!", ""]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_markdown_syntax(self):
        text = "# Heading\n* Bullet\n**Bold Text**\n_Emphasized Text_"
        expected = ["# Heading", "* Bullet", "**Bold Text**", "_Emphasized Text_"]
        self.assertEqual(markdown_to_blocks(text), expected)

if __name__ == "__main__":
    unittest.main()