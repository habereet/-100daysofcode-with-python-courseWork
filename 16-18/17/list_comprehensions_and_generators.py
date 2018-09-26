from pprint import pprint as pp
import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos', 'julian sequeira', 'sandra bullock', 'keanu reeves', 'julbob pybites', 'bob belderbos', 'julian sequeira', 'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

pp(f'Original NAMES List: ')
pp(NAMES)

# List Comprehension to upper case first and last names
print(f'\nList Comprehension to upper case first and last names in NAMES list')
pp([f'{name.split()[0].title()} {name.split()[1].title()}' for name in NAMES])

# List Comprehension to reverse first and last names
print(f'\nList Comprehension to reverse first and last names in NAMES list')
pp([f'{name.split()[1]} {name.split()[0]}' for name in NAMES])

# List Comprehension to reverse first and last names AND upper case them
print(f'\nList Comprehension to reverse first and last names AND upper case them')
pp([f'{name.split()[1].title()} {name.split()[0].title()}' for name in NAMES])


def gen_pairs():
	while True:
		while True:
			first_name = random.choice(NAMES).split()[0].title()
			second_name = random.choice(NAMES).split()[0].title()
			if first_name != second_name:
				break
			# Bob Belderbos used the following 3 lines in place of my above 4:
			#first, second = None, None
        	#while first == second: 
            	#first, second = random.sample(first_names, 2)
			#else:
				#print(f'duplicate, erasing: \'{first_name} teams up with {second_name}\'')
		yield print(f'{first_name} teams up with {second_name}')

NUM=10

pairs = gen_pairs()
#for _ in range(10):
    #next(pairs)
# -- OR -- LIST COMPREHENSION
[next(pairs) for _ in range(10)]

#print()
#[next(pairs) for _ in pairs]