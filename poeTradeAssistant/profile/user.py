import requests
import json
from poeTradeAssistant.db.setACCOUNT_NAME import setACCOUNT_NAME
from poeTradeAssistant.db.setPOESESSID import setPOESESSID
from poeTradeAssistant.db.retrieveCharacters import retrieveCharacters
from poeTradeAssistant.profile.character import Character

class User():
    def __init__(self, accountName, poesessid):
        setACCOUNT_NAME(accountName)
        setPOESESSID(poesessid)
        
        self.accountName = accountName
        self.poesessid = poesessid
        self.characters = retrieveCharacters()
        for character in self.characters:
            character.user = self

    def __str__(self):
        return "Account Name : " + self.accountName