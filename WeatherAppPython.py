
import requests

API_KEY = "082f8bbf4bffd19402ae3d6ffa37773d"

print("Welcome to Weather Forecast")

while True:
    city = input("Please Enter city Name (Or type end to quit): ").strip()
    
    if city.lower() == "end":
        print("Exiting the Weather Forecast!")
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
      temperature = data["main"]["temp"]
      humidity    = data["main"]["humidity"]
      description = data["weather"][0]["description"]
      wind_speed  = data["wind"]["speed"]

      print(f"\nWeather Report for {city}:")
      print(f"Temperature : {temperature}°C")
      print(f"Humidity    : {humidity}%")
      print(f"Condition   : {description}")
      print(f"Wind Speed  : {wind_speed} m/s")
    else:
      print("City not found or Input Error.. Please Try Again")
