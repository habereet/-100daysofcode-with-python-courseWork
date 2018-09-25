from load_rolls import read_rolls


class Roll:
    def __init__(self, name):
        self.name = name
        self.loses_to = read_rolls(name)
