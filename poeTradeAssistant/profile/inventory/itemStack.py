class ItemStack():
    def __init__(self, item, x, y, stackSize, maxStackSize):
        self.item = item
        self.x = x
        self.y = y
        self.stackSize = stackSize
        self.maxStackSize = maxStackSize
        self.tab = None

    def getPosition(self):
        return (x, y)