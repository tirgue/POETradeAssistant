class UserNotLoggedIn(Exception):
    def __init__(self):
        super().__init__("POESESSID not valid")