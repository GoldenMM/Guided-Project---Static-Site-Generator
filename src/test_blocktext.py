import unittest
from blocktext import *
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
    
class TestHeadToHtml(unittest.TestCase):
    def test_valid_head_block(self):
        block = "# This is a heading"
        expected = ParentNode(tag='h1', children=[LeafNode(tag=None, value="This is a heading")])
        self.assertEqual(head_to_html(block), expected)

    def test_invalid_head_block(self):
        block = "This is not a heading"
        with self.assertRaises(ValueError):
            head_to_html(block)

    def test_invalid_head_level(self):
        block = "####### This is a heading with invalid level"
        with self.assertRaises(ValueError):
            head_to_html(block)

class TestParaToHtml(unittest.TestCase):
    def test_valid_para_block(self):
        block = "This is a paragraph."
        expected = ParentNode(tag='p', children=[LeafNode(tag=None, value="This is a paragraph.")])
        self.assertEqual(para_to_html(block), expected)

    def test_invalid_para_block(self):
        block = "# This is not a paragraph"
        with self.assertRaises(ValueError):
            para_to_html(block)

class TestCodeToHtml(unittest.TestCase):
    def test_valid_code_block(self):
        block = "```print('Hello, World!')```"
        expected = ParentNode(tag="pre", children=[ParentNode(tag="code", children=[LeafNode(tag=None, value="print('Hello, World!')")])])
        self.assertEqual(code_to_html(block), expected)

    def test_invalid_code_block(self):
        block = "print('Hello, World!')"
        with self.assertRaises(ValueError):
            code_to_html(block)

class TestQuoteToHtml(unittest.TestCase):
    def test_valid_quote_block(self):
        block = "> This is a quote"
        expected = ParentNode(tag="blockquote", children=[LeafNode(tag=None, value="This is a quote")])
        self.assertEqual(quote_to_html(block), expected)

    def test_invalid_quote_block(self):
        block = "This is not a quote"
        with self.assertRaises(ValueError):
            quote_to_html(block)

    def test_multiple_lines_quote_block(self):
        block = "> This is a quote\n> with multiple lines\n> that are quoted"
        expected = ParentNode(tag="blockquote", children=[LeafNode(tag=None, value="This is a quote with multiple lines that are quoted")])
        self.assertEqual(quote_to_html(block), expected)
        
class TestUlistToHtml(unittest.TestCase):
    def test_valid_unordered_list_block(self):
        block = "* Item 1\n* Item 2"
        expected = ParentNode(tag="ul", children=[ParentNode(tag="li", children=[LeafNode(tag=None, value="Item 1")]), ParentNode(tag="li", children=[LeafNode(tag=None, value="Item 2")])])
        self.assertEqual(ulist_to_html(block), expected)

    def test_invalid_unordered_list_block(self):
        block = "1. Item 1\n2. Item 2"
        with self.assertRaises(ValueError):
            ulist_to_html(block)

class TestOlistToHtml(unittest.TestCase):
    def test_valid_ordered_list_block(self):
        block = "1. Item 1\n2. Item 2"
        expected = ParentNode(tag="ol", children=[ParentNode(tag="li", children=[LeafNode(tag=None, value="Item 1")]), ParentNode(tag="li", children=[LeafNode(tag=None, value="Item 2")])])
        self.assertEqual(olist_to_html(block), expected)

    def test_invalid_ordered_list_block(self):
        block = "* Item 1\n* Item 2"
        with self.assertRaises(ValueError):
            olist_to_html(block)
         
if __name__ == "__main__":
    unittest.main()