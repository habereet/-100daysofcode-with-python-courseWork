from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

names = 'pybites mike bob julian tim sara guido'.split()
print(names)
for name in names:
	print(name.title())

first_half_alphabet = list(string.ascii_lowercase)[:13]
print(first_half_alphabet)

new_names=[]
for name in names:
	if name[0] in first_half_alphabet:
		new_names.append(name.title())
print(new_names)

# --OR--

new_names = [name.title() for name in names if name[0] in list(string.ascii_lowercase)[:13]]
print(new_names)