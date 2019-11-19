class SimpleIterator:
    def __init__(self,tab):
        self.array = tab
        self.current_id = None

    def first(self):
        self.current_id = 0

    def next(self):
        self.current_id += 1

    def is_done(self):
        return self.current_id > len(self.array) - 1

    def current_item(self):
        return self.array[self.current_id]

    def __iter__(self):
        self.first()
        return self

    def __next__(self):
        if self.is_done():
            raise StopIteration
        else:
            result = self.current_item()
            self.next()
            return result

