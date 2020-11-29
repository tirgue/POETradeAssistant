from poeTradeAssistant.profile.inventory.item import Item
from poeTradeAssistant.shop.currency import Currency

class Offer():
    def __init__(self, item, nbItems, price, stock, currency):
        self.item = item
        self.nbItems = nbItems
        self.price = price
        self.stock = stock
        self.currency = currency 

    def __repr__(self):
        return {
            "item": {
                "name": self.item.name,
                "type": self.item.type,
                "icon": self.item.icon
            },
            "nbItems": self.nbItems,
            "price": self.price,
            "stock": self.stock,
            "currency": self.currency.value
        }

    def __str__(self):
        return str(self.__repr__())

    def priceTag(self):
        return "~b/o %s/%s %s" %(self.price, self.nbItems, self.currency.value)

    def fillOffer(self):
        result = ""
        items = self.shop.character.inventory.findMainTab(self.item)
        count = 0
        for item in items:
            if count < self.stock:
                result += f'[linkItem location="MainInventory" character="{self.shop.character.name}" x="{item.x}" y="{item.y}"]'
                count += item.stackSize

            else: break

        items = self.shop.character.inventory.findStashTabs(self.item)
        for item in items:
            if count < self.stock:
                result += f'[linkItem location="Stash{item.tab.index + 1}" league="{self.shop.character.league}" x="{item.x}" y="{item.y}"]'
                count += item.stackSize
            
            else: break

        return result

    def embed(self):
        return f'{self.__repr__()}\n[spoiler="{self.priceTag()}"]\n\n{self.fillOffer()}\n\n[/spoiler]\n\n'

    @staticmethod
    def fromJSON(json):
        return Offer(Item.fromJSON(json['item']), json['nbItems'], json['price'], json['stock'], Currency(json['currency']))