'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

def prep_log_file():
	# prep: read in the logfile
	logfile = "C:\\temp\\log"
	urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)
	
	with open(logfile) as f:
		loglines = f.readlines()
		shutdown_lines = []
		for line in loglines:
			if (line.find(SHUTDOWN_EVENT) != -1):
				shutdown_lines.append(convert_to_datetime(line))
	return shutdown_lines

def convert_to_datetime(line):
	return datetime.strptime(re.match('(^\S*?)\s([\:\-\dT]*)\s(supybot)\s(.*$)', line).group(2), "%Y-%m-%dT%H:%M:%S")
	

def time_between_shutdowns(loglines):
	return(loglines[1] - loglines[0])


def main():
	print(time_between_shutdowns(prep_log_file()))

if __name__ == '__main__':
	main()