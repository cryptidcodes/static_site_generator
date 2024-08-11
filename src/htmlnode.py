class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        HTMLlist = []
        for key in self.props:
            HTMLlist.append(f' {key}="{self.props[key]}"')
        HTMLlist = "".join(HTMLlist)
        return HTMLlist    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        # renders a leaf node as an HTML string
        if self.value == None:
            raise ValueError("**ERROR: value not found")
        elif self.tag == None:
            return self.value
        elif self.tag == "a":
            return f'<{self.tag} href="{self.props["href"]}">{self.value}</{self.tag}>'
        elif self.tag == "img":
            return f'<{self.tag} src="{self.props["src"]}" alt="{self.props["alt"]}">'
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag == None:
            raise ValueError("**ERROR: tag not found")
        elif self.children == None:
            raise ValueError("**ERROR: children not found")
        else:
            childlist = []
            for child in self.children:
                 childlist.append(f"{child.to_html()}")
            result = "".join(childlist)
            return f"<{self.tag}>{result}</{self.tag}>"
        