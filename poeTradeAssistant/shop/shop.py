import re
import requests
from poeTradeAssistant.db.updateShop import updateShop

class Shop():
    def __init__(self, shopId, shopHash):
        self.shopId = shopId
        self.shopHash = shopHash
        self.offers = []

    def addOffer(self, offer):
        self.offers.append(offer)
        offer.shop = self

    def embed(self):
        tag = "***DO NOT EDIT MANUALLY***\n"
        result = tag
        for offer in self.offers:
            result += offer.embed()

        result += "\n" + tag
        return result
        
    def update(self):
        updateShop(self)

