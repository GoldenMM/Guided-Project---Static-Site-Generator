
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props == None:
            return ""
        return_string = ""
        for key, value in self.props.items():
            return_string += f' {key}="{value}"'
        return return_string
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def __eq__(self, value: object) -> bool:
        return self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        children_html = []
        for child in self.children:
            if child.children == None:
                children_html.append(child.to_html())
            else:
                children_html.extend(child.to_html())
        return f"<{self.tag}{self.props_to_html()}>{''.join(children_html)}</{self.tag}>"

    def pretty_print(self, indent=0):
        ret_string = self.__repr__() + "\n"
        for child in self.children:
            if child.children == None:
                ret_string += "  " * indent + f"----{child.__repr__()}\n"
            else:
                ret_string += "  " * indent + f"----{child.pretty_print(indent + 1)}\n"
        return ret_string
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"