import poeTradeAssistant.db as db

def updateShop(shop):
    url = "https://www.pathofexile.com/forum/edit-thread/" + str(shop.shopId)
    rep = db.SESSION.post(
        url = url,
        data = {
            "title": "POETradeAssistant Shop",
            "content": shop.embed(),
            "notify_owner": "0",
            "hash": shop.shopHash,
            "post_submit": "Submit"
        }
    )