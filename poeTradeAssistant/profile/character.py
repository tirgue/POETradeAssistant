import requests
import json
from poeTradeAssistant.db.retrieveInventory import retrieveInventory
from poeTradeAssistant.db.retrieveShop import retrieveShop
from poeTradeAssistant.profile.inventory import MainTab
from poeTradeAssistant.profile.inventory import StashTab
from poeTradeAssistant.profile.inventory import Inventory


class Character():
    def __init__(self, name, league, level):
        self.name = name
        self.league = league
        self.level = level
        self.inventory = retrieveInventory(self.name, league)
        self.inventory.character = self

    def setShop(self, shopId):
        self.shop = retrieveShop(shopId)
        self.shop.character = self
    
    def __str__(self):
        return "%s : %s - lvl %s" %(self.name, self.league, self.level)