from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import TextNode
from inlinetext import split_nodes_delimiter, split_nodes_images, split_nodes_links
import enum

class BlockType(enum.Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(text):
    lines = text.split("\n")
    blocks = []
    for line in lines:
        if line == "":
            continue
        blocks.append(line.strip())
    return blocks
