from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import TextNode
from inlinetext import split_nodes_delimiter, split_nodes_images, split_nodes_links
import enum
import regex as re
import textwrap

class BlockType(enum.Enum):
    PARA = "paragraph"
    HEAD = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(text):
    split_text = textwrap.dedent(text).split("\n\n")
    blocks = []
    for block in split_text:
        if block == "":
            continue
        # Normalise white space of all lines in block
        block = re.sub(r"\s{2,}", "\n", block)
        blocks.append(block.strip())
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
        if not line[0] == str(count) or line[1] != ".":
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
    # UNORDERED LIST
    for line in block.split("\n"):
        if line[0] == "*" or line[0] == "-":
            return BlockType.ULIST
    # ORDERED LIST is now working??
    if is_ordered_list(block):
        return BlockType.OLIST
    return BlockType.PARA

#TODO: implement this function
def block_to_html(block):
    pass
