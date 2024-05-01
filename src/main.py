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
    md = "Hello, **world**! *Goodbye, world!*"
    print(print(split_nodes_delimiter([TextNode(md, "text")], "**", "bold")))

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
            return new_nodes # if the node is not text, add it to the new nodes
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
            

if __name__ == "__main__":
    main()