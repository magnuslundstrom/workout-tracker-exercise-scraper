import json


def find_unique_muscle_groups(): 

	with open('write.json', 'r') as f:
		data = json.load(f)

	unique_muscle_groups = []

	for exercise in data:
		if exercise['muscle_group'] not in unique_muscle_groups:
			unique_muscle_groups.append(exercise['muscle_group'])

	return unique_muscle_groups


def write_muscle_groups():	
	muscle_groups = find_unique_muscle_groups()

	writeFile = open('muscle_groups.json', 'w', encoding='utf8')
	json.dump(muscle_groups, writeFile, ensure_ascii=False)
	writeFile.close()
