from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from inlinetext import split_nodes_delimiter, split_nodes_images, split_nodes_links

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
    img_test = "IGNORE THIS PART ![image1](url1). AND THIS ![image2](url2)"
    img_test_no_img = "THIS IS A TEST"
    link_test = "IGNORE THIS PART [link1](url1). AND THIS [link2](url2)"
    
    for node in split_nodes_images([TextNode(img_test, "text")]):
        print(node)   

if __name__ == "__main__":
    main()