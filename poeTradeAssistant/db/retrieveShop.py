import requests
import re
import poeTradeAssistant.db as db
from poeTradeAssistant.db import POESESSID
from poeTradeAssistant.shop.shop import Shop

def retrieveShop(shopId):
    url = f"https://www.pathofexile.com/forum/edit-thread/{shopId}"
    rep = requests.get(
        url = url,
        headers={
            "cookie": "POESESSID=" + db.POESESSID
        }
    )       

    if rep.status_code != 200:
        raise Exception("POESESSID invalid")

    else:
        match = re.search("\*\*\*DO NOT DELETE THAT LINE\*\*\*\n((.|\n)*)\*\*\*DO NOT DELETE THAT LINE\*\*\*", rep.text)

        if match:
            text = match.group(1)

            shop = Shop(shopId, text)

            return shop

        else:
            raise Exception("SHOPID invalid")