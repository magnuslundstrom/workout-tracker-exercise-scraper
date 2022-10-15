import mysql.connector
import json
from utils import get_exercises, get_db

def save_to_db():
	db = get_db()
	cursor = db.cursor()

	exercises = map(lambda a: [a], get_exercises(1))
	sql = "INSERT INTO exercises (name) VALUES (%s)"

	print(exercises)




save_to_db()