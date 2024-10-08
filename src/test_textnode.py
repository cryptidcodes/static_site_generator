import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a test node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq6(self):
        node = TextNode("This is a test node", "italic", "https://www.boot.dev")
        node2 = TextNode("This is a test node", "italic", "https://www.boob.dev")
        self.assertNotEqual(node, node2)
    
    def test_eq7(self):
        node = TextNode("This is a test node", "italic", "https://www.boot.dev")
        node2 = TextNode("This is a test node", "italic")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()