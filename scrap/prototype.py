from abc import ABC

class WebSite(ABC):
    """
    Definition: prototype for scrapped websites that will be included dynamically.
    Every website class included must extend this and implement it's methods
    """

    def __init__(self, url):
        self.url = url

    def scrap(self, product, **kwargs):
        pass
