import re
from textnode import TextNode


text_type_text = "text"
text_type_italic = "italic"
text_type_bold = "bold"
text_type_code = "code"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        #for each node in the list old nodes, if the node is not a text type, append to a new list without transforming
        if node.text_type != text_type_text:
            new_nodes.append(node)

        #otherwise: if the node is a text type that does not contain the delimiter, append it to the list
        #elif delimiter not in node.text:
            #new_nodes.append(node)

        #otherwise seperate the enclosed string within the delimiter
        else:
            current_item = 0
            for item in node.text.split(f"{delimiter}"):
                if current_item % 2 == 0:
                    new_nodes.append(TextNode(item, text_type_text))
                    current_item += 1
                else:
                    new_nodes.append(TextNode(item, text_type))
                    current_item += 1


    #return a list of text nodes with delimiter split and named
    return new_nodes