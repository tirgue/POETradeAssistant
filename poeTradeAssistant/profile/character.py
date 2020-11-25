import requests
import json
from poeTradeAssistant.profile.UserNotLoggedIn import UserNotLoggedIn


class Character():
    def __init__(self, name, league, level):
        self.name = name
        self.league = league
        self.level = level

    def retrieveInventory(self, accountName, poesessid):
        backpackUrl = f"https://www.pathofexile.com/character-window/get-items?accountName={accountName}&character={self.name}"
        rep = requests.get(
            url = backpackUrl,
            headers={
                "cookie" : "POESESSID=" + poesessid
            }
        )

        rep = json.loads(rep.text)

        if list(rep)[0] == "error":
            raise UserNotLoggedIn()

        else:
            pass

    
    def __str__(self):
        return "%s : %s - lvl %s" %(self.name, self.league, self.level)