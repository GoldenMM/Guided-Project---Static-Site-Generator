from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from inlinetext import split_nodes_delimiter, split_nodes_images, split_nodes_links
from blocktext import markdown_to_blocks, BlockType, block_to_block_type, block_to_html
import textwrap

def main():
    text_node = TextNode("Hello, World!", "text")
    leaf_node = LeafNode(tag='p', value='Hello, world!')
    
    block_test = """ # This is a heading

    This is **bolded** paragraph

    This is another paragraph with *italic* text and `code` here
    This is the same paragraph on a new line

    * This is a list
    * with items
    
    
    1. This is an ordered list
    2. with items
    3. that are numbered 
    
    ```
    print('Hello, World!')
    ```
    
    > This is a quote
    > with multiple lines
    > that are quoted
    """
    
    for block in markdown_to_blocks(block_test):
        print(block)
        print(block_to_block_type(block))
        print("\n")

if __name__ == "__main__":
    
    main()