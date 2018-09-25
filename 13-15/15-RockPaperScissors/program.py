from rolls import Roll
from players import Player
import random


def print_header():
    print(f"-------------------------------------------------------")
    print(f"                      Welcome to")
    print(f"                Rock, Paper, Scissors")
    print(f"-------------------------------------------------------")


def get_user_name():
    player_one = Player(input("\nWhat is your name? "))
    return player_one


def output_match(player_one, player_two):
    print(f"Hello {player_one.name}, you'll be playing against {player_two.name}")


def get_computer_roll():
    return random.choice([Roll("Rock"), Roll("Gun"), Roll("Lightning"), Roll("Devil"), Roll("Dragon"),
                          Roll("Water"), Roll("Air"), Roll("Paper"), Roll("Sponge"), Roll("Wolf"),
                          Roll("Tree"), Roll("Human"), Roll("Snake"), Roll("Scissors"), Roll("Fire")])


def get_player_roll():
    roll_dict = {1: "Rock", 2: "Gun", 3: "Lightning", 4: "Devil", 5: "Dragon", 6: "Water", 7: "Air", 8: "Paper", 9: "Sponge", 10: "Wolf", 11: "Tree", 12: "Human", 13: "Snake", 14: "Scissors", 15: "Fire"}
    choice = 0
    print("")
    while not isinstance(choice, int) or choice not in range(1, 16):
        print(f"Choose your roll:")
        for roll in sorted(roll_dict.keys()):
            print(f" {roll:2d}: {roll_dict[roll]}")
        choice = int(input(f"Enter a number between 1 and 15: "))
        #if choice == 0:
        #    print(f'')
    return Roll(roll_dict[choice])


def play_game(player_two, score, game_length):
    count = 1
    while count <= game_length:
        p2_roll = get_computer_roll()
        p1_roll = get_player_roll()
        print(f"You played {p1_roll.name} and {player_two.name} played {p2_roll.name}.")
        if p2_roll.name in p1_roll.loses_to:
            print(f"You lost that round.")
            count += 1
            score.append((0, 1))
        elif p2_roll.name == p1_roll.name:
            print(f"That was a tie. We'll redo that round.")
        else:
            print(f"You won that round.")
            score.append((1, 0))
            count += 1
    return score


def calculate_score(score):
    pone = 0
    ptwo = 0
    for one, two in score:
        pone += one
        ptwo += two
    if pone == ptwo:
        print(f'\nYou tied {pone}-{ptwo}.')
    elif pone > ptwo:
        print(f'\nYou won that match {pone}-{ptwo}.')
    else:
        print(f'\nYou lost that match {pone}-{ptwo}.')


def choose_game_size():
    while True:
        print("")
        try:
            choice = int(input(f'Enter the number of rounds you would like this match to be: '))
        except ValueError:
            pass
        else:
            break
    return choice


def main():
    print_header()
    game_rolls = []
    player_one = get_user_name()
    player_two = Player()
    game_length = choose_game_size()
    output_match(player_one, player_two)
    raw_score = play_game(player_two, game_rolls, game_length)
    calculate_score(raw_score)


if __name__ == '__main__':
    main()
