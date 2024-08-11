import re
from textnode import TextNode


text_type_text = "text"
text_type_italic = "italic"
text_type_bold = "bold"
text_type_code = "code"
text_type_image = "image"
text_type_link = "link"

def extract_markdown_images(text):
    #takes raw markdown text and returns a list of tuples
    #each tuple should contain the alt text and url of any images

    if isinstance(text, str):
        return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    else:
        raise Exception("Extract Image requires a text input")

def extract_markdown_links(text):
    #takes raw markdown text and returns a list of tuples
    #each tuple should contain the anchor text and url of any links
    if isinstance(text, str):
        return re.findall(r"\[(.*?)\]\((.*?)\)", text)
    else:
        raise Exception("Extract Link requires a text input")

def split_nodes_image(old_nodes):
    #expects a list input (old_nodes)

    #initialize variable to store output
    new_nodes = []
    for node in old_nodes:
        #for each node in the list old nodes, if the node is not a text type, append to a new list without transforming
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            #extract images from the node into a list
            images = extract_markdown_images(node.text)
            #create a copy of the text in a new variable to iterate over
            remaining_text = node.text
            for image in images:
                #for each image if there is text preceding it, append as a textnode with text_type_text to new_nodes
                if remaining_text.split(f"![{image[0]}]({image[1]})")[0] != "":
                    new_nodes.append(
                        TextNode(remaining_text.split(f"![{image[0]}]({image[1]})")[0], 
                                text_type_text)
                        )
                #then append the image as a textnode with text_type_image to new_nodes
                new_nodes.append(
                    TextNode(image[0], text_type_image, image[1])
                    )
                #set the remaining_text variable to the text following the image
                remaining_text = remaining_text.split(f"![{image[0]}]({image[1]})")[1]
            #after iterating through all images, append any remaining text to new_nodes
            if remaining_text != "":
                new_nodes.append(TextNode(f"{remaining_text}", text_type_text))

    return new_nodes

def split_nodes_link(old_nodes):
    #expects a list input (old_nodes)

    #initialize variable to store output
    new_nodes = []
    for node in old_nodes:
        #for each node in the list old nodes, if the node is not a text type, append to a new list without transforming
        if node.text_type != text_type_text:
            new_nodes.append(node)
        else:
            #extract links from the node into a list
            links = extract_markdown_links(node.text)
            #create a copy of the text in a new variable to iterate over
            remaining_text = node.text
            for link in links:
                #for each link if there is text preceding it, append as a textnode with text_type_text to new_nodes
                if remaining_text.split(f"[{link[0]}]({link[1]})")[0] != "":
                    new_nodes.append(
                        TextNode(remaining_text.split(f"[{link[0]}]({link[1]})")[0], text_type_text)
                        )
                #then append the image as a textnode with text_type_image to new_nodes
                new_nodes.append(
                    TextNode(link[0], text_type_link, link[1])
                    )
                #set the remaining_text variable to the text following the image
                remaining_text = remaining_text.split(f"[{link[0]}]({link[1]})")[1]
            #after iterating through all images, append any remaining text to new_nodes
            if remaining_text != "":
                new_nodes.append(TextNode(remaining_text, text_type_text))

    return new_nodes