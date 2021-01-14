class EndOfTheList(Exception):
    def __init__(self, message="Used all words from the list"):
        self.message = message
        super().__init__(self.message)
