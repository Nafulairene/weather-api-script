import requests

# Replace with your actual API key from OpenWeather
API_KEY = "157205ce54e1fbcbf59522ecb21d3027"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Ask the user for a city
city = input("Enter a city name: ")

# Build the full request URL
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

# Send GET request
response = requests.get(url)

# Check for success
if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"The weather in {city} is {description} with a temperature of {temp}°C.")
else:
    print("Error: Could not retrieve weather data. Check your city name or API key.")
