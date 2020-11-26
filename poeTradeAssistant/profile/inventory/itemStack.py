class ItemStack():
    def __init__(self, item, stackSize, maxStackSize):
        self.item = item
        self.stackSize = stackSize
        self.maxStackSize = maxStackSize