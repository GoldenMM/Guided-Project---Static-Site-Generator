import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        text_node1 = TextNode("Hello, World!", "text")
        text_node2 = TextNode("Hello, World!", "text")
        self.assertEqual(text_node1, text_node2)
    
    def test_repr(self):
        text_node = TextNode("Hello, World!", "text")
        self.assertEqual(repr(text_node), "TextNode(Hello, World!, text, None)")
        
    def test_url_eq(self):
        text_node1 = TextNode("Hello, World!", "text", "https://www.example.com")
        text_node2 = TextNode("Hello, World!", "text", "https://www.example.com")
        self.assertEqual(text_node1, text_node2)
    
    def test_not_eq(self):
        text_node1 = TextNode("Hello, World!", "text")
        text_node2 = TextNode("Hello, World!", "text", "https://www.example.com")
        self.assertNotEqual(text_node1, text_node2)




if __name__ == "__main__":
    unittest.main()