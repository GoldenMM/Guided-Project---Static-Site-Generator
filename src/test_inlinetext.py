# FILEPATH: /home/xerxes/Documents/Boot.dev/Guided Project - Static Site Generator/src/test_main.py

import unittest
from inlinetext import split_nodes_images, split_nodes_links, text_to_text_nodes, split_nodes_delimiter, TextType
from textnode import TextNode

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_no_delimiter(self):
        nodes = [TextNode("Hello, World!", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, nodes)

    def test_split_nodes_delimiter_correct_usage(self):
        nodes = [TextNode("Hello, **World**!", TextType.TEXT)]
        expected_result = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("World", TextType.BOLD),
            TextNode("!", TextType.TEXT)
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, expected_result)

    def test_split_nodes_delimiter_incorrect_usage(self):
        nodes = [TextNode("Hello, **World!", TextType.TEXT)]
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertTrue('Invalid markdown syntax' in str(context.exception))


class TestSplitNodesImages(unittest.TestCase):
    def test_split_nodes_images_no_images(self):
        nodes = [TextNode("Hello, World!", TextType.TEXT)]
        result = split_nodes_images(nodes)
        self.assertEqual(result, nodes)

    def test_split_nodes_images_with_images(self):
        nodes = [TextNode("Hello, ![World](https://www.example.com/world.png)!", TextType.TEXT)]
        expected_result = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("World", TextType.IMG, "https://www.example.com/world.png"),
            TextNode("!", TextType.TEXT)
        ]
        result = split_nodes_images(nodes)
        self.assertEqual(result, expected_result)

    def test_split_nodes_images_multiple_images(self):
        nodes = [TextNode("Hello, ![World](https://www.example.com/world.png)![Universe](https://www.example.com/universe.png)!", TextType.TEXT)]
        expected_result = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("World", TextType.IMG, "https://www.example.com/world.png"),
            TextNode("Universe", TextType.IMG, "https://www.example.com/universe.png"),
            TextNode("!", TextType.TEXT)
        ]
        result = split_nodes_images(nodes)
        self.assertEqual(result, expected_result)

class TestSplitNodesLinks(unittest.TestCase):
    def test_split_nodes_links_no_links(self):
        nodes = [TextNode("Hello, World!", TextType.TEXT)]
        result = split_nodes_links(nodes)
        self.assertEqual(result, nodes)

    def test_split_nodes_links_with_one_link(self):
        nodes = [TextNode("Hello, [World](https://www.example.com/world)!", TextType.TEXT)]
        expected_result = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("World", TextType.LINK, "https://www.example.com/world"),
            TextNode("!", TextType.TEXT)
        ]
        result = split_nodes_links(nodes)
        self.assertEqual(result, expected_result)

    def test_split_nodes_links_with_multiple_links(self):
        nodes = [TextNode("Hello, [World](https://www.example.com/world)[Universe](https://www.example.com/universe)!", TextType.TEXT)]
        expected_result = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("World", TextType.LINK, "https://www.example.com/world"),
            TextNode("Universe", TextType.LINK, "https://www.example.com/universe"),
            TextNode("!", TextType.TEXT)
        ]
        result = split_nodes_links(nodes)
        self.assertEqual(result, expected_result)


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes_plain_text(self):
        text = "Hello, World!"
        expected_result = [TextNode("Hello, World!", TextType.TEXT)]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_bold_text(self):
        text = "Hello, **World**!"
        expected_result = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("World", TextType.BOLD),
            TextNode("!", TextType.TEXT)
        ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_italic_text(self):
        text = "Hello, *World*!"
        expected_result = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("World", TextType.ITALIC),
            TextNode("!", TextType.TEXT)
        ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_code_text(self):
        text = "Hello, `World`!"
        expected_result = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("World", TextType.CODE),
            TextNode("!", TextType.TEXT)
        ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_image(self):
        text = "Hello, ![World](https://www.example.com/world.png)!"
        expected_result = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("World", TextType.IMG, "https://www.example.com/world.png"),
            TextNode("!", TextType.TEXT)
        ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_link(self):
        text = "Hello, [World](https://www.example.com/world)!"
        expected_result = [
            TextNode("Hello, ", TextType.TEXT),
            TextNode("World", TextType.LINK, "https://www.example.com/world"),
            TextNode("!", TextType.TEXT)
        ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_multiple_syntax(self):
        text = "Hello, **World** and *Universe*!"
        expected_result = [
        TextNode("Hello, ", TextType.TEXT),
        TextNode("World", TextType.BOLD),
        TextNode(" and ", TextType.TEXT),
        TextNode("Universe", TextType.ITALIC),
        TextNode("!", TextType.TEXT)
    ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_multiple_links(self):
        text = "Hello, [World](https://www.example.com/world) and [Universe](https://www.example.com/universe)!"
        expected_result = [
        TextNode("Hello, ", TextType.TEXT),
        TextNode("World", TextType.LINK, "https://www.example.com/world"),
        TextNode(" and ", TextType.TEXT),
        TextNode("Universe", TextType.LINK, "https://www.example.com/universe"),
        TextNode("!", TextType.TEXT)
    ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)

    def test_text_to_text_nodes_multiple_images(self):
        text = "Hello, ![World](https://www.example.com/world.png) and ![Universe](https://www.example.com/universe.png)!"
        expected_result = [
        TextNode("Hello, ", TextType.TEXT),
        TextNode("World", TextType.IMG, "https://www.example.com/world.png"),
        TextNode(" and ", TextType.TEXT),
        TextNode("Universe", TextType.IMG, "https://www.example.com/universe.png"),
        TextNode("!", TextType.TEXT)
    ]
        result = text_to_text_nodes(text)
        self.assertEqual(result, expected_result)
    
if __name__ == "__main__":
    unittest.main()