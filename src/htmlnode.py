#from textnode import TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_string = ""
        for prop in self.props:
            props_string += f' {prop}="{self.props[prop]}"'
        return props_string

    def __repr__(self):
        return f'HTMLNode: {self.tag}, {self.value}, {self.children}, {self.props}'
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.value is None:
            return ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

    def to_html(self):
        if self.tag is None:
            html_string = ''
            raise ValueError("Invalid HTML: no tag")
        elif self.children is None:
            raise ValueError("Invalid HTML: no children")
        else:
            html_string = f'<{self.tag}>'
            for child in self.children:
                html_string += child.to_html()
            html_string += f'</{self.tag}>'
        return html_string