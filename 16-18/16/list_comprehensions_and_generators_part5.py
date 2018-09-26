from collections import Counter
import calendar
import itertools
import random
import re
import string
import timeit

import requests

from pprint import pprint as pp

def leap_years_lst(n=1000000):
	leap_years = []
	for year in range(1, n + 1):
		if calendar.isleap(year):
			leap_years.append(year)
	return leap_years

def leap_years_gen(n=1000000):
	for year in range(1, n + 1):
		if calendar.isleap(year):
			yield year


t=timeit.Timer(stmt="""\
leap_years = []
for year in range(1, 1000001):
	if calendar.isleap(year):
		leap_years.append(year)
""")
t.timeit(1)
#print(timeit(leap_years_gen()))

