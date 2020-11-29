from poeTradeAssistant.profile.inventory.item import Item
from poeTradeAssistant.shop.currency import Currency

class Offer():
    def __init__(self, item, nbItems, price, currency):
        self.item = item
        self.nbItems = nbItems
        self.price = price
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
            "currency": self.currency.value
        }

    def __str__(self):
        return str(self.__repr__())

    def priceTag(self):
        return "~b/o %s/%s %s" %(self.price, self.nbItems, self.currency.value)

    @staticmethod
    def fromJSON(json):
        return Offer(Item.fromJSON(json['item']), json['nbItems'], json['price'], Currency(json['currency']))