from .tab import Tab
import requests

class StashTab(Tab):
    def __init__(self, index):
        super().__init__(12, 12)
        self.index = index

    def retrieveItems(self, accountName, league, poesessid):
        url = f"https://www.pathofexile.com/character-window/get-stash-items?league={league}&accountName={accountName}&tabs=0&tabIndex={self.index}"
        rep = requests.get(
            url = url,
            headers={
                "cookie": "POESESSID=" + poesessid
            }
        )

        self.__processRep__(rep)
