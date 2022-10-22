from utils import get_exercises, get_db
import json


def save_to_db():
    db = get_db()
    cursor = db.cursor()

    # exercises = map(
    #     lambda a: [
    #         a["title"],
    #         a["image"] if "image" in a else None,
    #         a["rating"],
    #         a["muscle_group"],
    #     ],
    #     get_exercises(),
    # )

	
    all_exercises = get_exercises()
    exercises = []

    for exercise in all_exercises:
        muscleGroup = exercise["muscle_group"].replace(" ", "_")
        exercises.append([
			exercise["title"],
			exercise["image"] if "image" in exercise else None,
			exercise["rating"],
			muscleGroup,
		])

	
	

    sql = "INSERT INTO exercises (name, image, rating, muscleGroup) VALUES (%s, %s, %s, %s)"

    cursor.executemany(sql, exercises)

    db.commit()

    print(cursor.rowcount, "was inserted.")

    cursor.close()
    db.close()


save_to_db()
