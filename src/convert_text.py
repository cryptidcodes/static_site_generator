from textnode import TextNode
from htmlnode import LeafNode
from split_nodes_delimiter import split_nodes_delimiter
from split_images_links import split_nodes_image, split_nodes_link

text_type_text = "text"
text_type_italic = "italic"
text_type_bold = "bold"
text_type_code = "code"
text_type_image = "image"
text_type_link = "link"

def text_node_to_html_node(text_node):
    text_types = ["text", "bold", "italic", "code", "link", "image"]
    if text_node.text_type not in text_types:
        raise Exception("text node unknown type")
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
    if text_node.text_type == "image":
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

def text_to_textnodes(text):

    return split_nodes_delimiter(
        split_nodes_delimiter(
            split_nodes_delimiter(
                split_nodes_link(
                    split_nodes_image(
                        [TextNode(text, text_type_text)]
                    )
                ), "`", text_type_code
            ), "**", text_type_bold
        ), "*", text_type_italic
    )

def extract_title(markdown):
    #pulls h1 header from the markdown file
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.lstrip("# ")
        raise Exception("ERROR: unable to extract title. no header found")

def markdown_to_blocks(markdown):
    #takes a raw markdown string i.e. a full document and returns a list of "block" strings
    return markdown.split("\n\n")

def block_to_block_type(block):
    if block.startswith("#"):
        return "heading"
    elif block.startswith("```"):
        return "code"
    elif block.startswith("> "):
        return "quote"
    elif block.startswith("* ") or block.startswith("- "):
        return "unordered_list"
    elif block.startswith("1. "):
        return "ordered_list"
    else:
        return "paragraph"
    
def text_to_children(text):
    child_list = []
    for node in text_to_textnodes(text):
            if node.text != "":
                child_list.append(text_node_to_html_node(node))
    return child_list

def test():
    pass