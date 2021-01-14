from .Exceptions.word_list_ex import *


class WordList:
    def __init__(self, file_path: str):
        self.active = True
        self.index = -1

        f = open(file_path, "r")
        self.list = f.read().split("\n")
        f.close()

    def get_next(self) -> str:
        self.index += 1
        if self.index >= self.list.__len__():
            self.active = False
            raise EndOfTheList()
        return self.list[self.index]
