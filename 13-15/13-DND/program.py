from actors import Creature, Wizard, Dragon
import random


def main():
    print_header()
    game_loop()


def print_header():
    print(f'----------------------')
    print(f'    WIZARD GAME')
    print(f'----------------------')
    print()


def game_loop():
    creatures = [
        Creature('Bat', 5),
        Creature('Toad', 1),
        Creature('Tiger', 12),
        Dragon('Black Dragon', 50, scaliness=2, breathes_fire=False),
        Wizard('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandalf', 75)

    while True:
        active_creature = random.choice(creatures)
        print(f'A {active_creature.name} of level {active_creature.level} has appeared from a dark and foggy forest...')
        print()

        cmd = input('Do you [A]ttack, [R]unaway, or [L]ook Around? ').lower()
        if cmd == 'a':
            attack_results = hero.attack(active_creature)
            if attack_results[0]:
                creatures.remove(active_creature)
                print(f"{hero.name} rolled a {attack_results[1]} and defeated the {active_creature.name}, who rolled a {attack_results[2]}!")
            else:
                print(f"You rolled a {attack_results[1]}, while the {active_creature.name} rolled a {attack_results[2]}.")
                print(f"{hero.name} has been dealt a defeat.")
        elif cmd == 'r':
            print(f'The wizard flees')
        elif cmd == 'l':
            print(f"{hero.name} sees:")
            for current_creature in creatures:
                print(f" * {current_creature.name} of level {current_creature.level}")
        else:
            print("OK, exiting game...")
            break

        if not creatures:
            print("You've defeated all the creatures.")
            break

    print(f'Good bye')


if __name__ == '__main__':
    main()
