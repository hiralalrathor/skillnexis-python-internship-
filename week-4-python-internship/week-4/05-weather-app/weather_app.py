"""
Mini Project Task: Build a Weather App using OpenWeather API.

Requires a free API key from https://openweathermap.org/api
Set it as an environment variable before running:
    export OPENWEATHER_API_KEY="your_api_key_here"     (macOS/Linux)
    $env:OPENWEATHER_API_KEY="your_api_key_here"        (Windows PowerShell)
"""

import os
import requests

API_KEY = os.environ.get("OPENWEATHER_API_KEY", "")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city, api_key):
    """Fetch current weather data for a city from the OpenWeather API."""
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Celsius
    }
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def display_weather(data):
    city_name = data.get("name", "Unknown")
    weather_desc = data["weather"][0]["description"].title()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]

    print(f"\nWeather in {city_name}:")
    print(f"Condition: {weather_desc}")
    print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")


def main():
    print("=== Weather App (OpenWeather API) ===")

    if not API_KEY:
        print("Error: No API key found.")
        print("Set the OPENWEATHER_API_KEY environment variable before running.")
        print("Get a free key at: https://openweathermap.org/api")
        return

    city = input("Enter a city name: ").strip()

    try:
        data = get_weather(city, API_KEY)
    except requests.exceptions.HTTPError:
        print(f"Error: Could not find weather data for '{city}'.")
        return
    except requests.exceptions.RequestException as e:
        print(f"Error: Network request failed ({e}).")
        return

    display_weather(data)


if __name__ == "__main__":
    main()
