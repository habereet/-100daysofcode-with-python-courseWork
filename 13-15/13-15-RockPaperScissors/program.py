from rolls import Scissors, Paper, Rock
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
    return random.choice([Rock(), Paper(), Scissors()])


def get_player_roll():
    choice = ""
    print("")
    while choice == "" or "rps".find(choice) == -1:
        choice = input(f"Choose your roll: [R]ock, [P]aper, or [S]cissors: ").lower()
    return Rock() if choice == "r" else Paper() if choice == "p" else Scissors()


def play_game(player_one, player_two, score):
    count = 1
    while count <= 3:
        p2_roll = get_computer_roll()
        p1_roll = get_player_roll()
        print(f"You played {p1_roll.name} and {player_two.name} played {p2_roll.name}.")
        if p2_roll.name == p1_roll.loses_to:
            print(f"You lost that round.")
            score -= 1
            count += 1
        elif p2_roll.name == p1_roll.name:
            print(f"That was a tie. We'll redo that round.")
        else:
            print(f"You won that round.")
            score += 1
            count += 1
    return score


def report_outcome(score):
    print("")
    if score == 3:
        print(f"You swept all 3 rounds of that match")
    elif score == 1:
        print(f"You won that match 2-1")
    elif score == -1:
        print(f"You lost that match 1-2")
    else:
        print(f"You lost all the rounds in that match")


def main():
    print_header()
    game_rolls = 0
    player_one = get_user_name()
    player_two = Player()
    output_match(player_one, player_two)
    report_outcome(play_game(player_one, player_two, game_rolls))


if __name__ == '__main__':
    main()
