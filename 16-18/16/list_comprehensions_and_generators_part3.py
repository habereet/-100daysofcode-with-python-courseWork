from collections import Counter
import calendar
import itertools
import random
import re
import string

import requests

def num_gen():
	for i in range(1,65):
		yield i

gen = num_gen()

print(53 in gen)

for i in gen:
	print(i)
	print(type(i))
	print(type(gen))

print(gen)

print(3 in gen)