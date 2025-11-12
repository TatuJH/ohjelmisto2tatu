import requests

#Tehtävä 12.1
print(requests.get("https://api.chucknorris.io/jokes/random").json()["value"])

#Tehtävä 12.2
api_key = ""
paikkakunta = input("Anna paikkakunta: ")
print(f'{requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}&units=metric&lang=fi").json()["weather"][0]["description"].capitalize()}, {requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}&units=metric&lang=fi").json()["main"]["temp"]}°C')