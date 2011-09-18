class Alternator(object):
    def __init__(self, *kargs):
        self.options = kargs
        self.current = 0

    def get(self):
        index = self.current
        self.current = (self.current + 1) % len(self.options)
        return self.options[self.current]

    def set(self, new_index):
        self.current = new_index % len(self.options)

