import requests
import json
import poeTradeAssistant.db as db
from poeTradeAssistant.profile import Character

def retrieveCharacters():
    url = "https://www.pathofexile.com/character-window/get-characters"
    rep = requests.get(
        url,
        headers = {
            "cookie" : "POESESSID=" + db.POESESSID
        }
    )

    rep = json.loads(rep.text)

    if list(rep)[0] == "error":
        raise Exception("POESESSID invalid")

    else:
        characters = []
        for character in rep:
            name = character['name']
            league = character['league']
            level = character['level']
            c = Character(name, league, level)
            characters.append(c)

        return characters