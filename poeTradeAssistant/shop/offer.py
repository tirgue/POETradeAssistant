class Offer():
    def __init__(self, item, nbItems, price, currency):
        self.item = item
        self.nbItems = nbItems
        self.price = price
        self.currency = currency 

    def priceTag(self):
        return "~b/o %s/%s %s" %(self.price, self.nbItems, self.currency.value)