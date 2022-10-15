import mysql.connector
import json

def get_exercises(fixed_amount):
	exercises_json = open('exercises.json')
	data = json.load(exercises_json)
	if fixed_amount:
		return data[:fixed_amount]

	return data


def get_muscle_groups():
	muscle_groups_json = open('muscle_groups.json')
	data = json.load(muscle_groups_json)
	return data


def get_db():
	try:
		db = mysql.connector.connect(
			host="localhost",
			user="root",
			password="workout",
			database="workout",
			port=3306
		)

		return db

	except mysql.connector.Error as err:
		print(err)		