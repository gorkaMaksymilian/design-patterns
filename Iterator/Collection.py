from NonZeroIterator import NonZeroIterator
from SimpleIterator import SimpleIterator

class Collection:
    def __init__(self,array):
        self.array = array

    def iterator(self):
        return SimpleIterator(self.array)

    def non_zero_iterator(self):
        return NonZeroIterator(self.array)
