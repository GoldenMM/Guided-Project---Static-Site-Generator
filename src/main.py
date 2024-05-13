from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
from inlinetext import *
from blocktext import *
import os
import shutil

def main():
    
    with open("content/index.md", "r") as f:
        markdown = f.read()
    # print(markdown_to_html_node(markdown).pretty_print())
    
    generate_pages_recursive("content", "template.html", "public")

def generate_pages_recursive(from_path, template_path, dest_path):
    for item in os.listdir(from_path):
        s = os.path.join(from_path, item)
        d = os.path.join(dest_path, item)
        if os.path.isdir(s):
            generate_pages_recursive(s, template_path, d)
        else:
            if item.endswith(".md"):
                generate_page(s, template_path, d)
            else:
                print(f"Copying {s} to {d}")
                shutil.copy(s, d)
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template.replace(r"{{ Title }}", title).replace(r"{{ Content }}", html)
    
    path_split = dest_path.split("/")
    for dir in path_split[:-1]:
        if not os.path.exists(dir):
            print(f"Creating directory {dir}")
            os.makedirs(dir)
    with open(dest_path, "w") as f:
        f.write(page)

def extract_title(markdown):
    if not markdown.startswith("# "):
        raise ValueError("Markdown must start with a title")
    return markdown.split("\n")[0][2:]

def copy_dir(src, dest):
    if not os.path.exists(dest):
        print(f"Creating directory {dest}")
        os.makedirs(dest)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_dir(s, d)
        else:
            print(f"Copying {s} to {d}")
            shutil.copy(s, d)

if __name__ == "__main__":
    
    main()