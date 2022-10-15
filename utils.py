import json

def get_exercises(fixed_amount):
	exercises_json = open('exercises.json')
	data = json.load(exercises_json)
	if fixed_amount:
		return data[:fixed_amount]

	return data


