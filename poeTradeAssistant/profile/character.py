import requests
import json
from poeTradeAssistant.profile.exception import UserNotLoggedIn
from poeTradeAssistant.profile.inventory.mainTab import MainTab
from poeTradeAssistant.profile.inventory.stashTab import StashTab
from .inventory.inventory import Inventory


class Character():
    def __init__(self, name, league, level):
        self.name = name
        self.league = league
        self.level = level
        self.inventory = Inventory()
    
    def __str__(self):
        return "%s : %s - lvl %s" %(self.name, self.league, self.level)