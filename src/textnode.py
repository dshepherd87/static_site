class TextNode:
    def __init__(self, text, type, url=None):
        self.text = text
        self.text_type = type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True 
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"