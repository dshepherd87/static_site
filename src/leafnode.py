class LeafNode(HTMLNode):
    def __init__(self):
        super().__init__(tag=None, value, props=None)

    def to_html(self):
        if self.value is None:
            return ValueError("This node is missing a value")
        if self.tag is None:
            return value
        return f'<{self.tag}>{self.props_to_html}{self.value}</{self.tag}>'