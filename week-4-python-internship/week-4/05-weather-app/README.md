# Mini Project Task: Weather App (OpenWeather API)

**Assignment:** Build a Weather App using OpenWeather API.

Fetches and displays the current weather (temperature, condition,
humidity, wind speed) for any city, using the OpenWeather API.

## Setup
1. Get a free API key at [openweathermap.org/api](https://openweathermap.org/api)
2. Install the `requests` library:
   ```bash
   pip install requests
   ```
3. Set your API key as an environment variable:
   ```bash
   # macOS/Linux
   export OPENWEATHER_API_KEY="your_api_key_here"

   # Windows (PowerShell)
   $env:OPENWEATHER_API_KEY="your_api_key_here"
   ```

## Concepts Used
- REST API calls with the `requests` library
- Environment variables for secure API key handling
- JSON response parsing
- Exception handling for network/API errors

## How to Run
```bash
python weather_app.py
```

## Example
```
=== Weather App (OpenWeather API) ===
Enter a city name: Bhopal

Weather in Bhopal:
Condition: Clear Sky
Temperature: 31.5°C (feels like 33.2°C)
Humidity: 45%
Wind Speed: 3.1 m/s
```

## Note
This script makes a live network call to the OpenWeather API, so it
needs internet access and a valid API key to run — it cannot be
tested in an offline sandbox, but the code is complete and ready to
run on your machine.
