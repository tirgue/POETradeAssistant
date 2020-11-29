import json

class Tab():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.itemStacks = []

    def addItemStack(self, itemStack):
        self.itemStacks.append(itemStack)
        itemStack.tab = self

    def find(self, item):
        result = []
        for itemStack in self.itemStacks:
            if item == itemStack.item:
                result.append(itemStack)

        return result
