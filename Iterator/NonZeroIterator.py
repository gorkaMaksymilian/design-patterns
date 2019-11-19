from SimpleIterator import SimpleIterator

class NonZeroIterator(SimpleIterator):
    def __init__(self,array):
        super().__init__(array)

    def __next__(self):
        while True:
            if self.is_done():
                raise StopIteration
            else:
                if self.current_item() != 0:
                    result = self.current_item()
                    self.next()
                    return result
                else:
                    self.next()








