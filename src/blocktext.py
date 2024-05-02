from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import TextNode
from inlinetext import split_nodes_delimiter, split_nodes_images, split_nodes_links
import enum
import regex as re

class BlockType(enum.Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(text):
    lines = text.split("\n\n")
    blocks = []
    for line in lines:
        if line == "":
            continue
        blocks.append(line.strip())
    return blocks

# Helper function to check if all lines in a block start with a certain character
def block_lines_startwith(block, char):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(char):
            return False
    return True

# Helper function to check if an ordered list is properly ordered
def is_ordered_list(block):
    lines = block.split("\n")
    count = 1
    for line in lines:
        if not line[0] == str(count):
            return False
        count += 1
    return True

def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEAD
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block_lines_startwith(block, ">"):
        return BlockType.QUOTE
    if block_lines_startwith(block, "*") or block_lines_startwith(block, "-"):
        return BlockType.ULIST
    if block[0].isdigit() and block[1] == "." and is_ordered_list(block):
        return BlockType.OLIST
    return BlockType.PARA

def block_to_html(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARA:
        return ParentNode("p", [LeafNode(None, block)])
    if block_type == BlockType.HEAD:
        level = 0
        while block[level] == "#":
            level += 1
        return ParentNode(f"h{level}", [LeafNode(None, block[level+1:].strip())])
    if block_type == BlockType.CODE:
        return ParentNode("code", [LeafNode(None, block[3:-3])])
    if block_type == BlockType.QUOTE:
        lines = block.split("\n")
        children = []
        for line in lines:
            children.append(LeafNode(None, line[2:].strip()))
        return ParentNode("blockquote", children)
    if block_type == BlockType.ULIST:
        lines = block.split("\n")
        children = []
        for line in lines:
            children.append(ParentNode("li", [LeafNode(None, line[2:].strip())]))
        return ParentNode("ul", children)
    if block_type == BlockType.OLIST:
        lines = block.split("\n")
        children = []
        for line in lines:
            children.append(ParentNode("li", [LeafNode(None, line[3:].strip())]))
        return ParentNode("ol", children)
