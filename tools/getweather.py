import requests

city = "London"
api_key = "YOUR_API_KEY"  # Get from https://openweathermap.org/api
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

res = requests.get(url).json()
print(f"{city}: {res['weather'][0]['description']}, {res['main']['temp']}°C")
