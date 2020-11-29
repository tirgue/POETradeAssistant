import re
import requests

class Shop():
    def __init__(self, shopId):
        self.shopId = shopId
        self.offers = []

    def addOfffer(self, offer):
        self.offers.append(offer)
        offer.shop = self

    def embed(self):
        tag = "***DO NOT EDIT MANUALLY***\n"
        result = tag
        for offer in self.offers:
            result += offer.embed()

        result += "\n" + tag
        return result
        
