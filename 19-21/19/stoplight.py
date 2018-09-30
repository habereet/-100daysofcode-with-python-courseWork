from itertools import cycle
from colorama import init, Fore
from datetime import datetime, timedelta
from time import sleep
from random import randint
import sys



def main():
	init(autoreset=True)
	color_names = cycle(["GREEN", "YELLOW", "RED"])
	color_instructions = {"GREEN": "--Go--", "YELLOW": "Wait..", "RED": "STOP!!"}
	color_wait = {"YELLOW": 5}
	end_time = datetime.now() + timedelta(minutes=1)
	while datetime.now() < end_time:
		current_color = next(color_names)
		sys.stdout.write(getattr(Fore, current_color) + f'\r{color_instructions[current_color]}')
		sys.stdout.flush()
		sleep(color_wait.get(current_color, randint(3,8)))


if __name__ == "__main__":
	main()