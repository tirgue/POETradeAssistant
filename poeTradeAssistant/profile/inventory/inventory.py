import requests
import json
from ..exception import UserNotLoggedIn
from .mainTab import MainTab
from .stashTab import StashTab

class Inventory():
    def __init__(self):
        self.mainTab = None
        self.stashTabs = []

    def retrieveInventoryTabs(self, accountName, name, league, poesessid):
        stashUrl = f"https://www.pathofexile.com/character-window/get-stash-items?league={league}&accountName={accountName}&tabs=0&tabIndex="
        rep = requests.get(
            url = stashUrl,
            headers={
                "cookie" : "POESESSID=" + poesessid
            }
        )

        rep = json.loads(rep.text)

        if list(rep)[0] == "error":
            raise UserNotLoggedIn()

        else:
            numTabs = rep['numTabs']

            self.mainTab = MainTab()
            self.mainTab.retrieveItems(accountName, name, poesessid)

            self.stashTabs = []

            for i in range(numTabs):
                stashTab = StashTab(i)
                stashTab.retrieveItems(accountName, league, poesessid)
                self.stashTabs.append(stashTab)

    def itemCount(self):
        pass