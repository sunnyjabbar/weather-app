import requests

API_KEY = "YOUR OPENWEATHERMAP_API_KEY"  # Replace with your OpenWeatherMap API key

city = input("Enter a city: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    temperature = data["main"]["temp"]
    condition = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print()
    print(f"Weather in {city}")
    print("--------------------")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} m/s")

else:
    print("City not found. Please check the city name.")