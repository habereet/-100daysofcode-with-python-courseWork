from datetime import datetime
from datetime import timedelta
import time

WORK_TIME = 25

MINOR_BREAK_TIME = 5

MAJOR_BREAK_TIME = 15

SLEEP_TIME = 1

POMODORO_COUNT = 4

def work_timer(start_time, iteration):
	print(f'Pomodoro {iteration} started at {print_time()}')
	run_timer(start_time, WORK_TIME)
	print(f'Pomodoro {iteration} ended at {print_time()}')

def break_timer(start_time, break_time):
	print(f'Break started at {print_time()}')
	run_timer(start_time, break_time)
	print(f'Break ended at {print_time()}')

def run_timer(start_time, wait_time):
	while True:
		if datetime.now() >= (start_time + timedelta(seconds=wait_time)):
			break
		else:
			time.sleep(SLEEP_TIME)

def print_time():
	return time.strftime("%H:%M:%S", time.localtime())


if __name__ == "__main__":
	for iteration in range(1, POMODORO_COUNT+1):
		work_timer(datetime.now(), iteration)
		break_timer(datetime.now(), MAJOR_BREAK_TIME if iteration == POMODORO_COUNT else MINOR_BREAK_TIME)
		