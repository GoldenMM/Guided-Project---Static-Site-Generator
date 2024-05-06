# FILEPATH: /home/xerxes/Documents/Boot.dev/Guided Project - Static Site Generator/src/test_blocktext.py

import unittest
from blocktext import markdown_to_blocks, BlockType, block_to_block_type, block_to_html
from htmlnode import ParentNode, LeafNode

class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_line(self):
        text = "Hello, World!"
        expected = ["Hello, World!"]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_multiple_lines(self):
        text = "Hello,\nWorld!"
        expected = ["Hello,\nWorld!"]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_leading_trailing_whitespace(self):
        text = "  Hello, World!  "
        expected = ["Hello, World!"]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_empty_lines(self):
        text = "\n\nHello,\n\nWorld!\n\n"
        expected = ["Hello,", "World!"]
        self.assertEqual(markdown_to_blocks(text), expected)

    def test_markdown_syntax(self):
        text = "# Heading\n* Bullet\n**Bold Text**\n_Emphasized Text_"
        expected = ["# Heading\n* Bullet\n**Bold Text**\n_Emphasized Text_"]
        self.assertEqual(markdown_to_blocks(text), expected)

class TestBlockToBlockType(unittest.TestCase):
    def test_head_block(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEAD)

    def test_code_block(self):
        block = "```print('Hello, World!')```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote_block(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list_block(self):
        block = "* Item 1\n* Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)

    def test_ordered_list_block(self):
        block = "1. Item 1\n2. Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)

    def test_paragraph_block(self):
        block = "This is a paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARA)

    def test_improperly_ordered_list(self):
        block = "1. Item 1\n3. Item 2"
        self.assertNotEqual(block_to_block_type(block), BlockType.OLIST)


if __name__ == "__main__":
    unittest.main()