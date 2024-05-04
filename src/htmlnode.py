class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    

    def to_html(self):
        raise NotImplementedError("Method to be implemented")
    

    def props_to_html(self):
        if self.props is None:
            return ""
        prop_html = ""
        for prop in self.props:
            prop_html += f' {prop}="{self.props[prop]}"'
        return prop_html
    

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"