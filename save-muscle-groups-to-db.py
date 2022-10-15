from utils import get_muscle_groups, get_db

def save_muscle_group_to_db():
	db = get_db()
	cursor = db.cursor()

	muscle_groups = map(lambda mg: [mg], get_muscle_groups())
	sql = "INSERT INTO muscleGroups (name) VALUES (%s)"
	cursor.executemany(sql, muscle_groups)

	db.commit()
	print(cursor.rowcount, "was inserted.")

	cursor.close()
	db.close()

save_muscle_group_to_db()
