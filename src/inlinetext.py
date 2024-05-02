from textnode import TextNode
from htmlnode import LeafNode, ParentNode, HTMLNode
import regex as re

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text)
    if text_node.text_type == "bold":
        return LeafNode("b", text_node.text)
    if text_node.text_type == "italic":
        return LeafNode("i", text_node.text)
    if text_node.text_type == "code":
        return LeafNode("code", text_node.text)
    if text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == "img":
        return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:  
        if node.text_type != "text":
            new_nodes.append(node)
            continue # if the node is not text, add it to the new nodes
        split_nodes = node.text.split(delimiter)
        # Check to see if the delimiter is used correctly
        if len(split_nodes) % 2 == 0:
            raise Exception("Invalid markdown syntax")
        # Odd indexes are the delimited text
        for i, split_node in enumerate(split_nodes):
            if i % 2 == 0:
                new_nodes.append(TextNode(split_node, "text"))
            else:
                new_nodes.append(TextNode(split_node, text_type))
    return new_nodes

def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        # extract the images from the text
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for image in images:
            split_nodes = remaining_text.split(f"![{image[0]}]({image[1]})", 1)
            if split_nodes[0] != "":
                new_nodes.append(TextNode(split_nodes[0], "text"))
            new_nodes.append(TextNode(image[0], "img", image[1]))
            remaining_text = split_nodes[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, "text"))
    return new_nodes
        
def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for link in links:
            split_nodes = remaining_text.split(f"[{link[0]}]({link[1]})", 1)
            if split_nodes[0] != "":
                new_nodes.append(TextNode(split_nodes[0], "text"))
            new_nodes.append(TextNode(link[0], "link", link[1]))
            remaining_text = split_nodes[1]
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, "text"))
    return new_nodes  

def text_to_text_nodes(text):
    nodes = [TextNode(text, 'text')]
    nodes = split_nodes_delimiter(nodes, "**", 'bold')
    nodes = split_nodes_delimiter(nodes, "*", 'italic')
    nodes = split_nodes_delimiter(nodes, "`", 'code')
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)
    return nodes

def extract_markdown_images(markdown):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", markdown)

def extract_markdown_links(markdown):
    return re.findall(r"\[(.*?)\]\((.*?)\)", markdown)