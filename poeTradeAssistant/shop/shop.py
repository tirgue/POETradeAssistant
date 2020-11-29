import re
import requests

class Shop():
    def __init__(self, shopId):
        self.shopId = shopId
        self.offers = []

    def addOfffer(self, offer):
        self.offers.append(offer)
