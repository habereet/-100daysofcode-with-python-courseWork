import random

class Creature:
    def __init__(self, name="Toad", level=1):
        self.name = name
        self.level = level

    def defensive_roll(self):
        roll = random.randint(1, 12)
        return roll * self.level

class Dragon(Creature):
    def __init__(self, name="Night Fury", level=1, scaliness=1, breathes_fire=False):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breathes_fire = breathes_fire

    def defensive_roll(self):
        roll = super().defensive_roll()
        value = roll * self.scaliness
        if self.breathes_fire:
            value = value * 2
        return value

class Wizard(Creature):
    def attack(self, creature):
        my_roll = self.defensive_roll()
        their_roll = creature.defensive_roll()

        return (my_roll >= their_roll, my_roll, their_roll)