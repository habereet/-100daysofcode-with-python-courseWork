cars = {
	'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
	'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
	'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
	'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
	'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
	"""return a comma  + space (', ') separated string of jeep models (original order)"""
	my_string = ""
	for index, model in enumerate(cars['Jeep']):
		my_string += model
		if index != len(cars['Jeep']) - 1:
			my_string += ", "
	return my_string


def get_first_model_each_manufacturer():
	"""return a list of matching models (original ordering)"""
	model_list = []
	for mfr in cars.keys():
		model_list.append(cars[mfr][0])
	return model_list


def get_all_matching_models(grep='trail'):
	"""return a list of all models containing the case insensitive
		'grep' string which defaults to 'trail' for this exercise,
		sort the resulting sequence alphabetically"""
	matching_models = []
	for mfr in cars.keys():
		for model in cars[mfr][0:]:
			if grep.lower() in model.lower():
				matching_models.append(model)
	return sorted(matching_models)


def sort_car_models():
	"""sort the car models (values) and return the resulting cars dict"""
	new_car = {}
	for mfr in sorted(cars.keys()):
		new_car[mfr] = sorted(cars[mfr])
	return new_car

def main():
	print(get_all_jeeps())
	print(get_first_model_each_manufacturer())
	print(get_all_matching_models())
	print(get_all_matching_models(grep='CO'))
	print(sort_car_models())


if __name__ == '__main__':
	main()