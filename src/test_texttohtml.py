import unittest

from textnode import TextNode

from main import text_node_to_html_node

class TestTextToHTML(unittest.TestCase):
    def test_text_to_HTML1(self):
        testtextnode1 = TextNode("This is regular text.", "text")
        if text_node_to_html_node(testtextnode1).to_html() != "This is regular text.":
            raise Exception("textnode to htmlnode conversion failed")

    def test_text_to_HTML2(self):
        testtextnode2 = TextNode("This is bold text.", "bold")
        if text_node_to_html_node(testtextnode2).to_html() != "<b>This is bold text.</b>":
            raise Exception("textnode to htmlnode conversion failed")
    
    def test_text_to_HTML3(self):
        testtextnode3 = TextNode("This is italic text.", "italic")
        if text_node_to_html_node(testtextnode3).to_html() != "<i>This is italic text.</i>":
            raise Exception("textnode to htmlnode conversion failed")
        
    def test_text_to_HTML4(self):
        testtextnode4 = TextNode("This is code.", "code")
        if text_node_to_html_node(testtextnode4).to_html() != "<code>This is code.</code>":
            raise Exception("textnode to htmlnode conversion failed")
        
    def test_text_to_HTML5(self):
        testtextnode5 = TextNode("This is a link.", "link", "https://www.boot.dev")
        if text_node_to_html_node(testtextnode5).to_html() != '<a href="https://www.boot.dev">This is a link.</a>':
            raise Exception("textnode to htmlnode conversion failed")

    def test_text_to_HTML6(self):
        testtextnode6 = TextNode("This is an image.", "image", "url/of/image.jpg")
        if text_node_to_html_node(testtextnode6).to_html() != '<img src="url/of/image.jpg" alt="This is an image.">':
            raise Exception("textnode to htmlnode conversion failed")


        