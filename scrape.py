import requests
import bs4
import json


urls = ['https://www.bodybuilding.com/exercises/finder/1']

# for i in range(1,212): 
# 	urls.append('https://www.bodybuilding.com/exercises/finder/'+str(i))


def scrape():

	for url in urls:
		res = requests.get(urls[0])
		soup = bs4.BeautifulSoup(res.text, 'html.parser')

		exercises = soup.find_all("div", class_="ExResult-row")

		print(exercises[0])

		for exercise in exercises:
			title = exercise.find("h3", class_="ExResult-resultsHeading").text.strip()
			muscle_group = exercise.find("div", class_="ExResult-muscleTargeted").text.replace("Muscle Targeted:", "").strip()
			print(muscle_group)

scrape()
