from htmlnode import LeafNode, ParentNode, HTMLNode
from textnode import TextNode
from inlinetext import *
import regex as re
import textwrap
import enum

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
    # HEAD
    if re.findall(r"^#{1,6} ", block):
        return BlockType.HEAD
    # CODE
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    # QUOTE
    if block_lines_startwith(block, ">"):
        return BlockType.QUOTE
    # UNORDERED LIST
    for line in block.split("\n"):
        if line[0] == "*" or line[0] == "-":
            return BlockType.ULIST
    # ORDERED LIST
    if is_ordered_list(block):
        return BlockType.OLIST
    return BlockType.PARA

def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def head_to_html(block):
    if block_to_block_type(block) != BlockType.HEAD:
        raise ValueError("Block is not a heading")
    level = len(re.findall(r"^#{1,6}", block)[0])
    if level not in range(1, 7):
        raise ValueError("Heading level must be between 1 and 6")
    return ParentNode(tag=f"h{level}", children=text_to_children(block[level+1:]))

def para_to_html(block):
    if block_to_block_type(block) != BlockType.PARA:
        raise ValueError("Block is not a paragraph")
    return ParentNode(tag="p", children=text_to_children(block))

def code_to_html(block):
    if block_to_block_type(block) != BlockType.CODE:
        raise ValueError("Block is not a code block")
    return ParentNode(tag="pre", children=[ParentNode(tag="code", children=text_to_children(block[3:-3]))])

def quote_to_html(block):
    if block_to_block_type(block) != BlockType.QUOTE:
        raise ValueError("Block is not a quote block")
    value = " ".join([line[2:] for line in block.split("\n")])
    return ParentNode(tag="blockquote", children=text_to_children(value))

def ulist_to_html(block):
    if block_to_block_type(block) != BlockType.ULIST:
        raise ValueError("Block is not an unordered list")
    children = []
    for line in block.split("\n"):
        children.append(ParentNode(tag="li", children=line[2:]))
    return ParentNode(tag="ul", children=children)

def olist_to_html(block):
    if block_to_block_type(block) != BlockType.OLIST:
        raise ValueError("Block is not an ordered list")
    children = []
    for line in block.split("\n"):
        children.append(ParentNode(tag="li", children=line[3:]))
    return ParentNode(tag="ol", children=children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARA:
        return para_to_html(block)
    if block_type == BlockType.HEAD:
        return head_to_html(block)
    if block_type == BlockType.CODE:
        return code_to_html(block)
    if block_type == BlockType.OLIST:
        return olist_to_html(block)
    if block_type == BlockType.ULIST:
        return ulist_to_html(block)
    if block_type == BlockType.QUOTE:
        return quote_to_html(block)
    raise ValueError("Invalid block type")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        children.append(block_to_html_node(block))
    return ParentNode(tag="div", children=children)
    