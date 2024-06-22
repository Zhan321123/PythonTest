from typing import Sequence

from .lineList import *


class Flat:
    def __init__(self, data: Sequence[Sequence]):
        self.data = data

    def get(self):
        pass

    def set(self, data: Sequence[Sequence]):
        pass

    def print(self):
        pass

    def printALl(self):
        pass


class FlatList(Flat):
    def __init__(self, data: Sequence[Sequence]):
        super().__init__(data)
