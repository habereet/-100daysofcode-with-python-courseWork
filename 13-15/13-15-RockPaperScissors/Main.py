def print_title():
    print(f'---------------------------')
    print(f'        Welcome to')
    print(f'   Rock, Paper, Scissors')
    print(f'---------------------------')


def get_user_name():
    return input("\nWhat is your name? ")


def output_name(name):
    print(f"Hello {name}")


def main():
    print_title()
    user = get_user_name()
    output_name(user)


if __name__ == '__main__':
    main()
