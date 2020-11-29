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
        match = re.search(f"{tag}\n((.|\n)*){tag}", rep.text)

        if match:
            body = match.group(1)
            match = re.findall("({.*})", body)

            if match:
                shop = Shop(shopId)

                for offer in match:
                    offer = offer.replace("&#039;","\"")
                    offer = json.loads(offer)
                    shop.offers.append(Offer.fromJSON(offer))

                return shop

        raise Exception("SHOPID invalid")