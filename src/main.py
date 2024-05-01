from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    text_node = TextNode("Hello, World!", "text")
    leaf_node = LeafNode(tag='p', value='Hello, world!')
    
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
    
    print(node.to_html())
    
if __name__ == "__main__":
    main()