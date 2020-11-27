import requests
import json

class Inventory():
    def __init__(self, mainTab, stashTabs):
        self.mainTab = mainTab
        self.stashTabs = stashTabs

    def itemCount(self):
        counter = {}
        allTabs = self.mainTab.itemsStack

        for stashTab in self.stashTabs:
            allTabs += stashTab.itemsStack

        for itemStack in allTabs:
            item = itemStack.item
            count = itemStack.stackSize

            if counter.get(item) == None:
                counter[item] = count
            
            else:
                counter[item] += count

        return counter