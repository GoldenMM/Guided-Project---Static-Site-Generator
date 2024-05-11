from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from inlinetext import *
from blocktext import *

def main():
    text_node = TextNode("Hello, World!", "text")
    leaf_node = LeafNode(tag='p', value='Hello, world!')
    
    block_test = """ Here we are only texting paragraphs
    
    This is a new paragraph
    
    This is a new paragraph with a [link](https://www.google.com)
    
    This is a new para with bold text **bold text** and italic text *italic text*.
    
    * This is a list
    * This is a list
    * This is a list
    
    1. This is an ordered list
    2. This is an ordered list
    """
    
    text_child = "This is a new para with bold text **bold text** and italic text *italic text*." 
    
    list_test = "* This is a list\n* This is a **bold** list\n* This is a list"
    
    # print (markdown_to_html_node(block_test))
    
    print (markdown_to_html_node(block_test).pretty_print())
    
    
if __name__ == "__main__":
    
    main()