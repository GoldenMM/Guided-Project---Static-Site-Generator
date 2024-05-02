from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import TextNode
from inlinetext import split_nodes_delimiter, split_nodes_images, split_nodes_links

def markdown_to_blocks(text):
    lines = text.split("\n")
    blocks = []
    for line in lines:
        if line == "":
            continue
        blocks.append(line.strip())
    return blocks