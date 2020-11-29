import requests
import json
import poeTradeAssistant.db as db
from ..profile.inventory.item import Item
from ..profile.inventory.itemStack import ItemStack
from ..profile.inventory.mainTab import MainTab
from ..profile.inventory.stashTab import StashTab

def retrieveTab(main, character = "", league = "", index = ""):
    if main:
        url = f"https://www.pathofexile.com/character-window/get-items?accountName={db.ACCOUNT_NAME}&character={character}"
    else:
        url = f"https://www.pathofexile.com/character-window/get-stash-items?league={league}&accountName={db.ACCOUNT_NAME}&tabs=0&tabIndex={index}"
    
    rep = requests.get(
        url = url,
        headers={
            "cookie": "POESESSID=" + db.POESESSID
        }
    )

    rep = json.loads(rep.text)

    if list(rep)[0] == "error":
        raise Exception("POESESSID invalid")

    else:

        if main:
            tab = MainTab()

        else:
            tab = StashTab(index)

        items = rep['items']
        for item in items:
            name = item['name']
            typeLine = item['typeLine']
            try:
                stackSize = item['stackSize']
                maxStackSize = item['maxStackSize']

            except :
                stackSize = 1
                maxStackSize = 1

            try:
                x = item['x']
                y = item['y']

            except :
                x = None
                y = None

            icon = item['icon']

            i = Item(name, typeLine, icon)
            iStack = ItemStack(i, x, y, stackSize, maxStackSize)
            tab.addItemStack(iStack)

        return tab        