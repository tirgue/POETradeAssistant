from .tab import Tab
import requests

class StashTab(Tab):
    def __init__(self, index):
        super().__init__(12, 12)
        self.index = index
