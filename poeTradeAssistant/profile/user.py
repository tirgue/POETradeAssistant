import requests
import json
from poeTradeAssistant.profile.UserNotLoggedIn import UserNotLoggedIn
from poeTradeAssistant.profile.character import Character

class User():
    def __init__(self, accountName, poesessid):
        self.accountName = accountName
        self.poesessid = poesessid
        self.__retrieveCharacters__()
        for character in self.characters:
            character.retrieveInventory(accountName, poesessid)

    def __retrieveCharacters__(self):
        url = "https://www.pathofexile.com/character-window/get-characters"
        rep = requests.get(
            url,
            headers = {
                "cookie" : "POESESSID=" + self.poesessid
            }
        )

        rep = json.loads(rep.text)

        if list(rep)[0] == "error":
            raise UserNotLoggedIn()

        else:
            self.characters = []
            for character in rep:
                name = character['name']
                league = character['league']
                level = character['level']
                c = Character(name, league, level)
                self.characters.append(c)
                