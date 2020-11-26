from .tab import Tab
import requests

class MainTab(Tab):
    def __init__(self):
        super().__init__(12, 5)

    def retrieveItems(self, accountName, character, poesessid):
        url = f"https://www.pathofexile.com/character-window/get-items?accountName={accountName}&character={character}"
        rep = requests.get(
            url = url,
            headers={
                "cookie": "POESESSID=" + poesessid
            }
        )

        self.__processRep__(rep)
        