import poeTradeAssistant.db as db

def setPOESESSID(poesessid):
    db.SESSION.headers.update({'cookie':'POESESSID='+poesessid})