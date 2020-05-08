import requests
from json import load

def tokens():  # Easier to work with jsons aka dictionaries
	with open("res/TOKENS.json", 'r') as FPtr:
		return load(FPtr)

def NewsFromBBC(): 

	main_url = tokens()["int_news_url"]
 
	open_bbc_page = requests.get(main_url).json() 
 
	article = open_bbc_page["articles"] 

	results = [] 
	data = ''

	for ar in article: 
		results.append(ar['title']) 
		  
	for i in range(len(results)): 
		data = data + str(i+1) + ') ' + str(results[i]) + '\n'
	
	return data

def indianNews():
	
	main_url = tokens()["ind_news_url"]

	news = requests.get(main_url).json()

	article = news["articles"]

	results = [] 
	data = ''
	  
	for ar in article: 
		results.append(ar['title']) 
		  
	for i in range(len(results)): 
		data = data + str(i+1) + ') ' + str(results[i]) + '\n'
	
	return data

def return_weather(city):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, tokens()["weather_token"])

	res = requests.get(url)

	data = res.json()

	try :
		temp = data['main']['temp']
		wind_speed = data['wind']['speed']
		description = data['weather'][0]['description']
		data = 'Weather in {} :\n'.format(city) + 'Temperature : {} °C\n'.format(temp) + 'Wind Speeds : {} m/s\n'.format(wind_speed) + 'Description : {}'.format(description)

	except KeyError :
		data = 'Please enter a valid city name'

	return data