import requests
import re
import json
import poeTradeAssistant.db as db
from poeTradeAssistant.db import POESESSID
from poeTradeAssistant.shop.shop import Shop
from poeTradeAssistant.shop.offer import Offer

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
        tag = "\*\*\*DO NOT EDIT MANUALLY\*\*\*"
        match = re.search(f"{tag}\n((.|\n)*){tag}\n", rep.text)

        if match:
            body = match.group(1)
            match = re.findall("({.*})", body)

            if match:
                shop = Shop(shopId)

                for offer in match:
                    offer = offer.replace("&#039;","\"")
                    offer = json.loads(offer)
                    offer = Offer.fromJSON(offer)
                    offer.shop = shop
                    shop.offers.append(offer)

                return shop

        raise Exception("SHOPID invalid")