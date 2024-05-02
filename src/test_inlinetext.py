# FILEPATH: /home/xerxes/Documents/Boot.dev/Guided Project - Static Site Generator/src/test_main.py

import unittest
from inlinetext import split_nodes_images, split_nodes_links, text_to_text_nodes
from textnode import TextNode

class TestSplitNodesImages(unittest.TestCase):
    def test_split_nodes_images_no_images(self):
        nodes = [TextNode("Hello, World!", "text")]
        result = split_nodes_images(nodes)
        self.assertEqual(result, nodes)

    def test_split_nodes_images_with_images(self):
        nodes = [TextNode("Hello, ![World](https://www.example.com/world.png)!", "text")]
        expected_result = [
            TextNode("Hello, ", "text"),
            TextNode("World", "img", "https://www.example.com/world.png"),
            TextNode("!", "text")
        ]
        result = split_nodes_images(nodes)
        self.assertEqual(result, expected_result)

    def test_split_nodes_images_multiple_images(self):
        nodes = [TextNode("Hello, ![World](https://www.example.com/world.png)![Universe](https://www.example.com/universe.png)!", "text")]
        expected_result = [
            TextNode("Hello, ", "text"),
            TextNode("World", "img", "https://www.example.com/world.png"),
            TextNode("Universe", "img", "https://www.example.com/universe.png"),
            TextNode("!", "text")
        ]
        result = split_nodes_images(nodes)
        self.assertEqual(result, expected_result)

class TestSplitNodesLinks(unittest.TestCase):
    def test_split_nodes_links_no_links(self):
        nodes = [TextNode("Hello, World!", "text")]
        result = split_nodes_links(nodes)
        self.assertEqual(result, nodes)

    def test_split_nodes_links_with_one_link(self):
        nodes = [TextNode("Hello, [World](https://www.example.com/world)!", "text")]
        expected_result = [
            TextNode("Hello, ", "text"),
            TextNode("World", "link", "https://www.example.com/world"),
            TextNode("!", "text")
        ]
        result = split_nodes_links(nodes)
        self.assertEqual(result, expected_result)

    def test_split_nodes_links_with_multiple_links(self):
        nodes = [TextNode("Hello, [World](https://www.example.com/world)[Universe](https://www.example.com/universe)!", "text")]
        expected_result = [
            TextNode("Hello, ", "text"),
            TextNode("World", "link", "https://www.example.com/world"),
            TextNode("Universe", "link", "https://www.example.com/universe"),
            TextNode("!", "text")
        ]
        result = split_nodes_links(nodes)
        self.assertEqual(result, expected_result)


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes_plain_text(self):
        text = "Hello, World!"
        expected_result = [TextNode("Hello, World!", "text")]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_bold_text(self):
        text = "Hello, **World**!"
        expected_result = [
            TextNode("Hello, ", "text"),
            TextNode("World", "bold"),
            TextNode("!", "text")
        ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_italic_text(self):
        text = "Hello, *World*!"
        expected_result = [
            TextNode("Hello, ", "text"),
            TextNode("World", "italic"),
            TextNode("!", "text")
        ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_code_text(self):
        text = "Hello, `World`!"
        expected_result = [
            TextNode("Hello, ", "text"),
            TextNode("World", "code"),
            TextNode("!", "text")
        ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_image(self):
        text = "Hello, ![World](https://www.example.com/world.png)!"
        expected_result = [
            TextNode("Hello, ", "text"),
            TextNode("World", "img", "https://www.example.com/world.png"),
            TextNode("!", "text")
        ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_link(self):
        text = "Hello, [World](https://www.example.com/world)!"
        expected_result = [
            TextNode("Hello, ", "text"),
            TextNode("World", "link", "https://www.example.com/world"),
            TextNode("!", "text")
        ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_multiple_syntax(self):
        text = "Hello, **World** and *Universe*!"
        expected_result = [
        TextNode("Hello, ", "text"),
        TextNode("World", "bold"),
        TextNode(" and ", "text"),
        TextNode("Universe", "italic"),
        TextNode("!", "text")
    ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_multiple_links(self):
        text = "Hello, [World](https://www.example.com/world) and [Universe](https://www.example.com/universe)!"
        expected_result = [
        TextNode("Hello, ", "text"),
        TextNode("World", "link", "https://www.example.com/world"),
        TextNode(" and ", "text"),
        TextNode("Universe", "link", "https://www.example.com/universe"),
        TextNode("!", "text")
    ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_multiple_images(self):
        text = "Hello, ![World](https://www.example.com/world.png) and ![Universe](https://www.example.com/universe.png)!"
        expected_result = [
        TextNode("Hello, ", "text"),
        TextNode("World", "img", "https://www.example.com/world.png"),
        TextNode(" and ", "text"),
        TextNode("Universe", "img", "https://www.example.com/universe.png"),
        TextNode("!", "text")
    ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)
    
if __name__ == "__main__":
    unittest.main()