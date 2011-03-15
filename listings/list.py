class FunctionalList:
    '''A class wrapping a list with some extra functional 
    magic, like head, tail, init, last, drop, and take.'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if key is of invalid type or value, the list values 
        # will raise the error
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):
        self.values.append(value)
    def head(self):
        # get the first element
        return self.values[0]
    def tail(self):
        # get all elements after the first
        return self.values[1:]
    def init(self):
        # get elements up to the last
        return self.values[:-1]
    def last(self):
        # get last element
        return self.values[-1]
    def drop(self, n):
        # get all elements except first n
        return self.values[n:]
    def take(self, n):
        # get first n elements
        return self.values[:n]
