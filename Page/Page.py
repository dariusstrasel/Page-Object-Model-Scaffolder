from .BasePage import BasePage


class Page(BasePage):
    """
    Represents any given HTML page on a website.
    """

    def __init__(self, url, elements, child_pages, source_html):
        print("Creating {self.tag_name} tag.")
        super().__init__(url, elements, child_pages, source_html)
