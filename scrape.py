import requests
import bs4
import json

AMOUNT_OF_PAGES = 212

urls = []
for i in range(1,AMOUNT_OF_PAGES): 
	urls.append('https://www.bodybuilding.com/exercises/finder/'+str(i))


def scrape():

	print("Starting to scrape " + str(AMOUNT_OF_PAGES) + " pages on bodybuilding.com for exercises")

	all_exercises = []
	stop = False

	for url in urls:
		if stop:
			break

		res = requests.get(url)
		print("Connecting to: ", url)
		soup = bs4.BeautifulSoup(res.text, 'html.parser')

		exercises = soup.find_all("div", class_="ExResult-row")	

		for exercise in exercises:
			try: 
				title = exercise.find("h3", class_="ExResult-resultsHeading").text.strip()
				muscle_group = exercise.find("div", class_="ExResult-muscleTargeted").text.replace("Muscle Targeted:", "").strip()
				image = exercise.find("img", class_="ExResult-img")['src']
				rating = float(exercise.find("div", class_="ExRating-badge").text.strip())

				if(rating < 4.0):
					stop = True
					break

				exercise_data = {
					'title': title,
					'muscle_group': muscle_group,
					'image': image,
					'rating': rating
				}

				all_exercises.append(exercise_data)
			except:
				pass

	print("Found " + str(len(all_exercises))  + " exercises above 4.0 rating")
	print("Writing to file...")
	writeFile = open('exercises.json', 'w', encoding='utf8')
	json.dump(all_exercises, writeFile, ensure_ascii=False)
	print("Done!")
	writeFile.close()

scrape()
