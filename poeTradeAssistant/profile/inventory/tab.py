import json
from .item import Item
from .itemStack import ItemStack
from ..exception import UserNotLoggedIn

class Tab():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # ABSTRACT
    def retrieveItems(self, accountName, poesessid):
        pass

    def __processRep__(self, rep):
        rep = json.loads(rep.text)

        if list(rep)[0] == "error":
            raise UserNotLoggedIn()

        else:
            self.itemsStack = []
            items = rep['items']
            for item in items:
                name = item['name']
                typeLine = item['typeLine']
                try:
                    stackSize = item['stackSize']
                    maxStackSize = item['maxStackSize']

                except :
                    stackSize = 1
                    maxStackSize = 1

                try:
                    x = item['x']
                    y = item['y']

                except :
                    x = None
                    y = None

                icon = item['icon']

                i = Item(name, typeLine, icon)
                iStack = ItemStack(i, x, y, stackSize, maxStackSize)
                self.itemsStack.append(iStack)