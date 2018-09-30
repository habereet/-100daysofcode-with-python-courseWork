from itertools import combinations, permutations

def friends_teams(list_of_friends, team_size = 2, order_does_matter = False):
	if not order_does_matter:
		return list(combinations(list_of_friends, team_size))
	else:
		return list(permutations(list_of_friends, team_size))


if __name__ == '__main__':
	print(friends_teams('Bob Dante Julian Martin'.split(), 2, False))
