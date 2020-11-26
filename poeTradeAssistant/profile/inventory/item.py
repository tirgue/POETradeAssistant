class Item():
    def __init__(self, name, typeLine, icon):
        self.name = name
        self.type = typeLine
        self.icon = icon

    def fullName(self):
        if self.name:
            return "%s, %s" %(self.name, self.type)

        else:
            return self.type

    def __eq__(self, value):
        if value is self:
            return True

        elif type(value) == Item:
            return self.name == value.name and self.type == value.type

        else:
            return False

    def __hash__(self):
        return hash((self.name, self.type))