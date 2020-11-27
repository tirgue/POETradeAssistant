from .tab import Tab
import requests

class StashTab(Tab):
    def __init__(self, index, itemStacks):
        super().__init__(12, 12, itemStacks)
        self.index = index
