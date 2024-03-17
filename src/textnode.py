class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        #checks that type is the same
        if not isinstance(other, type(self)):
            return False
        #Compares the values
        return self.value == other.value
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
