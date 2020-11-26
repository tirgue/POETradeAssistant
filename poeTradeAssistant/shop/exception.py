class InvalidThreadNumber(Exception):
    def __init__(self):
        super().__init__("The thread id supplied is incorrect")