import requests
import bs4
import json


urls = []
for i in range(1,212): 
	urls.append('https://www.bodybuilding.com/exercises/finder/'+str(i))


def scrape():

	all_exercises = []

	for url in urls:
		res = requests.get(url)
		print("connecting to: ", url)
		soup = bs4.BeautifulSoup(res.text, 'html.parser')

		exercises = soup.find_all("div", class_="ExResult-row")

	

		for exercise in exercises:
			try: 
				title = exercise.find("h3", class_="ExResult-resultsHeading").text.strip()
				muscle_group = exercise.find("div", class_="ExResult-muscleTargeted").text.replace("Muscle Targeted:", "").strip()
				image = exercise.find("img", class_="ExResult-img")['src']

				exercise_data = {
					'title': title,
					'muscle_group': muscle_group,
					'image': image
				}

				all_exercises.append(exercise_data)
			except:
				pass

	writeFile = open('exercises.json', 'w', encoding='utf8')
	json.dump(all_exercises, writeFile, ensure_ascii=False)
	writeFile.close()

scrape()
