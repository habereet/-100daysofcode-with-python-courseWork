names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
	while len(names) < max(len(names), len(locations), len(confirmed)):
		names.append('-')
	while len(locations) < max(len(names), len(locations), len(confirmed)):
		locations.append('-')
	while len(confirmed) < max(len(names), len(locations), len(confirmed)):
		confirmed.append('-')
	for participant in zip(names, locations, confirmed):
		print(participant)


if __name__ == '__main__':
	get_attendees()