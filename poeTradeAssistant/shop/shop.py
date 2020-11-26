import re
import requests
from ..profile.exception import UserNotLoggedIn
from .exception import InvalidThreadNumber

class Shop():
    def __init__(self, character, threadNumber):
        self.character = character
        self.url = f"https://www.pathofexile.com/forum/edit-thread/{threadNumber}"

    def retrieveShopInfo(self, poesessid):
        rep = requests.get(
            url = self.url,
            headers={
                "cookie": "POESESSID=" + poesessid
            }
        )       

        if rep.status_code != 200:
            raise UserNotLoggedIn()

        else:
            match = re.search("\*\*\*DO NOT DELETE THAT LINE\*\*\*\n((.|\n)*)\*\*\*DO NOT DELETE THAT LINE\*\*\*", rep.text)

            if match:
                self.text = match.group(1)

            else:
                raise InvalidThreadNumber()