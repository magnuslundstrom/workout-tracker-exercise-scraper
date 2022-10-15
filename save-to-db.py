import mysql.connector
import json
from utils import get_exercises

def save_to_db():
	try:

		db = mysql.connector.connect(
			host="localhost",
			user="root",
			password="",
			database="mydatabase"
		)

		cursor = db.cursor()



	except mysql.connector.Error as err:
		print(err)

