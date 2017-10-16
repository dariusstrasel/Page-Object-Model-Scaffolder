from .BaseElement import BaseElement


class A(BaseElement):
    """
    Anchor HTML element.
    """
    tag_name = "a"
    attributes = {"url": "www.google.com"}

    def __init__(self):
        print("Creating {self.tag_name} tag.")
        super().__init__(self.attributes, self.tag_name)


class Input(BaseElement):
    """
    Input HTMl element.
    """
    tag_name = "input"
    attributes = None

    def __init__(self):
        print("Creating {self.tag_name} tag.")
        super().__init__(self.attributes, self.tag_name)