import requests
import json
import poeTradeAssistant.db as db
from poeTradeAssistant.db.retrieveTab import retrieveTab
from poeTradeAssistant.profile.inventory import MainTab
from poeTradeAssistant.profile.inventory import StashTab
from poeTradeAssistant.profile.inventory import Inventory

def retrieveInventory(character, league):
    mainTab = retrieveTab(True, character, league)
    stashTabs = []
    url = f"https://www.pathofexile.com/character-window/get-stash-items?league={league}&accountName={db.ACCOUNT_NAME}&tabs=0&tabIndex=0"
    rep = db.SESSION.get(url)

    rep = json.loads(rep.text)

    if list(rep)[0] == "error":
        raise Exception("POESESSID invalid")

    else:
        numTabs = rep['numTabs']

    for i in range(numTabs):
        stashTab = retrieveTab(False, character, league, i)
        stashTabs.append(stashTab)

    return Inventory(mainTab, stashTabs)