from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

from pprint import pprint as pp

def create_select_options(options):
	select_list = []
	for option in options:
		select_list.append(f'<option value={option}>{option.title()}</option>')
	return(select_list)

# -- OR --

def create_select_options_2(options):
	for option in options:
		yield f'<option value={option}>{option.title()}</option>'

options = 'red yellow blue purple black white'.split()
pp(create_select_options(options))

# Generators are 'lazy' so you have to iterate on them
print(create_select_options_2(options))
pp(list(create_select_options_2(options)))
