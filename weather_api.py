import requests
import json

api_key = "d4e35b305668a9e8de533df5e33bec5c"
base_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city: ")

url = f"{base_url}?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

if(data["cod"] == 200):
    main = data["main"]
    weather = data["weather"][0]

    print(f"City: {city.title()}")
    print(f"Temperature: {main['temp']} celsius")
    print(f"Humidity: {main['humidity']}%")
    print(f"Condition: {weather['description'].title()}")

else:
    print("City not found")