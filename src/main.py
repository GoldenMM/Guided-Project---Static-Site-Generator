from textnode import TextNode
from htmlnode import HTMLNode, LeafNode

def main():
    text_node = TextNode("Hello, World!", "text")
    leaf_node = LeafNode(tag='p', value='Hello, world!')
    
    print(leaf_node.to_html())
    
if __name__ == "__main__":
    main()