from htmlnode import ParentNode
from convert_text import block_to_block_type, text_to_children, markdown_to_blocks

def markdown_to_html_node(markdown):
    #converts a full markdown document into a single HTMLNode containing all child HTMLNodes of each element
    blocks = markdown_to_blocks(markdown)
    nodelist = []
    for block in blocks:
        if block_to_block_type(block) == "heading":
            tag = f"h{len(block.split()[0])}"
            child_list = text_to_children(block.lstrip("#").lstrip(" "))
            nodelist.append(ParentNode(tag, child_list))
        if block_to_block_type(block) == "unordered_list":
            outertag = "ul"
            innertag = "li"
            outerlist = []
            for item in block.split("\n"):
                innerlist = text_to_children(item.lstrip("* "))
                outerlist.append(ParentNode(innertag, innerlist))
            nodelist.append(ParentNode(outertag, outerlist))
        if block_to_block_type(block) == "ordered_list":
            outertag = "ol"
            innertag = "li"
            outerlist = []
            splitblock = block.split("\n")
            for item in splitblock:
                innerlist = text_to_children(item.lstrip(f"{splitblock.index(item)+1}. "))
                outerlist.append(ParentNode(innertag, innerlist))
            nodelist.append(ParentNode(outertag, outerlist))
        if block_to_block_type(block) == "code":
            code = text_to_children(block.lstrip("```\n").rstrip("\n```"))
            nodelist.append(ParentNode("code", code))
        if block_to_block_type(block) == "quote":
            quotelist = block.split("> ")
            for quotes in quotelist:
                if not quotes == "":
                    quote = text_to_children(quotes.lstrip("> "))
                    nodelist.append(ParentNode("blockquote", quote))
        if block_to_block_type(block) == "paragraph":
            paragraph = text_to_children(block)
            nodelist.append(ParentNode("p", paragraph))

    return ParentNode("div", nodelist)

def test():
    markdown_to_html_node(
        """# The Unparalleled Majesty of "The Lord of the Rings"

[Back Home](/)

![LOTR image artistmonkeys](/images/rivendell.png)

> "I cordially dislike allegory in all its manifestations, and always have done so since I grew old and wary enough to detect its presence.
> I much prefer history, true or feigned, with its varied applicability to the thought and experience of readers.
> I think that many confuse 'applicability' with 'allegory'; but the one resides in the freedom of the reader, and the other in the purposed domination of the author."

In the annals of fantasy literature and the broader realm of creative world-building, few sagas can rival the intricate tapestry woven by J.R.R. Tolkien in *The Lord of the Rings*. You can find the [wiki here](https://lotr.fandom.com/wiki/Main_Page)."""
    )
test()