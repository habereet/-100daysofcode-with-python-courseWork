class Roll:
    def __init__(self, name):
        self.name = name


class Paper(Roll):
    def __init__(self, name="Paper"):
        super().__init__(name)
        self.loses_to = "Scissors"


class Rock(Roll):
    def __init__(self, name="Rock"):
        super().__init__(name)
        self.loses_to = "Paper"


class Scissors(Roll):
    def __init__(self, name="Scissors"):
        super().__init__(name)
        self.loses_to = "Rock"
