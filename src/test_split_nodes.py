import unittest

from convert_text import text_to_textnodes, markdown_to_blocks, block_to_block_type, extract_title
from textnode import TextNode
from split_nodes_delimiter import split_nodes_delimiter
from split_images_links import extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link

text_type_text = "text"
text_type_italic = "italic"
text_type_bold = "bold"
text_type_code = "code"
text_type_image = "image"
text_type_link = "link"

class TestSplitNodes(unittest.TestCase):
    def testsplitnodes1(self):
        node = TextNode(
                "This is a test. The **bold text here** should be seperated into a **bold** node. The *italic text here* should be seperated into an *italic* node. The `code block here` should be seperated into a `code block` node.",
            text_type_text
        )
        nodelist = [node]
        testcase = (
            split_nodes_delimiter(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        nodelist,

                        "`",
                        text_type_code),

                        "**",
                        text_type_bold),

                        "*",
                        text_type_italic)
            )
        if testcase != [TextNode("This is a test. The ", "text", None), 
                        TextNode("bold text here", "bold", None), 
                        TextNode(" should be seperated into a ", "text", None), 
                        TextNode("bold", "bold", None), 
                        TextNode(" node. The ", "text", None), 
                        TextNode("italic text here", "italic", None), 
                        TextNode(" should be seperated into an ", "text", None), 
                        TextNode("italic", "italic", None), 
                        TextNode(" node. The ", "text", None), 
                        TextNode("code block here", "code", None), 
                        TextNode(" should be seperated into a ", "text", None), 
                        TextNode("code block", "code", None), 
                        TextNode(" node.", "text", None)
                        ]:
            raise Exception("split nodes delimiter fn failed!")
        

class TestExtractImagesAndLinks(unittest.TestCase):
    def testextractimages1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        if extract_markdown_images(text) != [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]:
            raise Exception("extract image from markdown failed")
    def testextractimages2(self):
        text = "This is text with a [rick roll](https://www.youtube.com/watch?v=dQw4w9WgXcQ)"
        if extract_markdown_images(text) != []:
            raise Exception("extract image from markdown failed")
    def testextractimages3(self):
        text = ""
        if extract_markdown_images(text) != []:
            raise Exception("extract image from markdown failed")
    def testextractlinks1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        if extract_markdown_links(text) != [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]:
            raise Exception("extract link from markdown failed")
    def testextractlinks2(self):
        text = "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)"
        if extract_markdown_links(text) != [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]:
            raise Exception("extract link from markdown failed")
    def testextractlinks3(self):
        text = ""
        if extract_markdown_links(text) != []:
            raise Exception("extract link from markdown failed")
        
class TestSplitImagesAndLinks(unittest.TestCase):
    def testsplitimageatend(self):
        node =[
            TextNode("This is a text with a ![markdown image](url/of/image.jpg)", text_type_text)
        ]
        if split_nodes_image(node) != [TextNode("This is a text with a ", "text", None), TextNode("markdown image", "image", "url/of/image.jpg")]:
            raise Exception("split image at end failed")
    def testsplitimageatfront(self):
        node =[
            TextNode("![markdown image](url/of/image.jpg) this is text with an image in front", text_type_text)
        ]
        if split_nodes_image(node) != [TextNode("markdown image", "image", "url/of/image.jpg"), TextNode(" this is text with an image in front", "text", None)]:
            raise Exception("split image at beginning failed")
    def testsplitimagesmultiple(self):
        node =[
            TextNode("![markdown image](url/of/image.jpg) this is text with an image in front, an image ![second markdown image](secondurl/of/image.jpg) in the middle, and an image at the end ![last markdown image](lasturl/of/image.jpg)", text_type_text)
        ]
        if split_nodes_image(node) != [
            TextNode("markdown image", "image", "url/of/image.jpg"), 
            TextNode(" this is text with an image in front, an image ", "text", None), 
            TextNode("second markdown image", "image", "secondurl/of/image.jpg"), 
            TextNode(" in the middle, and an image at the end ", "text", None), 
            TextNode("last markdown image", "image", "lasturl/of/image.jpg")
            ]:
            raise Exception("splitting multiple images failed")
    def testsplitlinkatend(self):
        node =[
            TextNode("This is a text with a [markdown link](https://www.google.com)", text_type_text)
        ]
        if split_nodes_link(node) != [
            TextNode("This is a text with a ", "text", None), 
            TextNode("markdown link", "link", "https://www.google.com")
            ]:
            raise Exception("split link at end failed")
    def testsplitlinkatfront(self):
        node =[
            TextNode("[markdown link](https://www.google.com) this is text with a link in front", text_type_text)
        ]
        if split_nodes_link(node) != [
            TextNode("markdown link", "link", "https://www.google.com"), 
            TextNode(" this is text with a link in front", "text", None)
            ]:
            raise Exception("split link at beginning failed")
    def testsplitlinksmultiple(self):
        node =[
            TextNode("[markdown link](https://www.google.com) this is text with a link in front, a link [second markdown image](https://www.boot.dev) in the middle, and a link at the end [last markdown image](https://www.twitch.tv)", text_type_text)
        ]
        if split_nodes_link(node) != [
            TextNode("markdown link", "link", "https://www.google.com"), 
            TextNode(" this is text with a link in front, a link ", "text", None), 
            TextNode("second markdown image", "link", "https://www.boot.dev"), 
            TextNode(" in the middle, and a link at the end ", "text", None), 
            TextNode("last markdown image", "link", "https://www.twitch.tv")
            ]:
            raise Exception("splitting multiple links failed")
        


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_nodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        if text_to_textnodes(text) != [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev")
            ]:
            raise Exception("Text to TextNode conversion failed")

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = (
        """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        )
        if markdown_to_blocks(text) != [
            '# This is a heading', 
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
            ]:
            raise Exception("markdown block conversion failed")
        
class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        blocks = [
            '# This is a heading', 
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item',
            '1. This is the first list item in an ordered list\n2. This is the second item\n3. This is the last item',
            '>This is a direct quote\n>this is the second line of quote',
            '````this is a block of code```',
            ]
        types = []
        for block in blocks:
            types.append(block_to_block_type(block))
        if types != ['heading', 'paragraph', 'unordered_list', 'ordered_list', 'quote', 'code']:
            raise Exception("unknown block type error")
        
class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = ("""# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item""")
        if extract_title(markdown) != "This is a heading":
            raise Exception("title extraction failed")