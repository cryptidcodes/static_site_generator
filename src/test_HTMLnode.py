import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "this is a value", None, {"href": "https://www.google.com", "target": "_blank",})
        if node.props_to_html() != ' href="https://www.google.com" target="_blank"':
            raise Exception("props_to_html failed")
        
    def test_props_to_html2(self):
        node = HTMLNode(None, None, None, {"href": "https://www.boot.dev", "target": "_planck",})
        if node.props_to_html() != ' href="https://www.boot.dev" target="_planck"':
            raise Exception("props_to_html failed")
        
class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "this is a value", {"href": "https://www.google.com", "target": "_blank",})
        if node.to_html() != "<p>this is a value</p>":
            raise Exception("leaf to_html failed")
        
    def test_to_html2(self):
        node = LeafNode(None, "Click Me!", {"href": "https://www.boot.dev", "target": "_planck",})
        if node.to_html() != "Click Me!":
            raise Exception("leaf to_html failed")
    
    def test_to_html3(self):
        node = LeafNode("a", "Click Me!", {"href": "https://www.boot.dev", "target": "_planck",})
        if node.to_html() != '<a href="https://www.boot.dev">Click Me!</a>':
            raise Exception("leaf to_html failed")
        
class TestParentNode(unittest.TestCase):
    def testParentNode1(self):
        node = ParentNode(
        "p",
        [
        LeafNode("b", "this is Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "this is italic text"),
        LeafNode(None, "Normal text"),
        LeafNode("a", "this is a link", {"href": "https://www.boot.dev"}),
        LeafNode(None, "Normal text"),
        ],
        )
        if node.to_html() != '<p><b>this is Bold text</b>Normal text<i>this is italic text</i>Normal text<a href="https://www.boot.dev">this is a link</a>Normal text</p>':
            raise Exception("parent to_html failed")
    def testParentNode2(self):
        node = ParentNode(
        "p",
        [
        LeafNode(None, "Normal text"),
        LeafNode("a", "this is a link", {"href": "https://www.boot.dev"}),
        LeafNode(None, "Normal text"),
        ],
        )
        node2 = ParentNode(
        "h",
        [
        LeafNode("b", "Bold text"), 
        node,
        LeafNode("i", "Italic text"),
        ],
        )
        if node2.to_html() != '<h><b>Bold text</b><p>Normal text<a href="https://www.boot.dev">this is a link</a>Normal text</p><i>Italic text</i></h>':
            raise Exception("parent to_html failed")
    def testParentNode3(self):
        node = ParentNode(
        "p",
        [],
        )
        if node.to_html() != '<p></p>':
            raise Exception("parent to_html failed")
    def testParentNode4(self):
        node = ParentNode(
        "p",
        [
        LeafNode(None, "Normal text"),
        LeafNode(None, "Normal text"),
        ],
        )
        node2 = ParentNode(
        "h",
        [
        LeafNode("b", "Bold text"),
        LeafNode("a", "this is a link", {"href": "https://www.boot.dev"}),
        LeafNode("i", "Italic text"),
        ],
        )
        node3 = ParentNode(
        "p",
        [
        LeafNode(None, "Normal text"),
        LeafNode(None, "Normal text"),
        LeafNode("b", "Bold text"),
        ],
        )
        node4 = ParentNode(
            "h",
            [
            node,
            node2,
            node3,
            ]
        )
        if node4.to_html() != '<h><p>Normal textNormal text</p><h><b>Bold text</b><a href="https://www.boot.dev">this is a link</a><i>Italic text</i></h><p>Normal textNormal text<b>Bold text</b></p></h>':
            raise Exception("parent to_html failed")
        
if __name__ == "__main__":
    unittest.main()