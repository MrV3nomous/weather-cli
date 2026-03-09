import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
from config import API_KEY  # Import API key from config.py

console = Console()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

# ------------------------
# Helper Functions
# ------------------------
def get_weather(city: str, unit: str = "metric"):
    params = {"q": city, "appid": API_KEY, "units": unit}
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error fetching weather:[/bold red] {e}")
        return None

def get_forecast(city: str, unit: str = "metric"):
    params = {"q": city, "appid": API_KEY, "units": unit}
    try:
        response = requests.get(FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        console.print(f"[bold red]Error fetching forecast:[/bold red] {e}")
        return None

def weather_emoji(description: str):
    desc = description.lower()
    if "cloud" in desc: return "☁️"
    if "rain" in desc: return "🌧"
    if "snow" in desc: return "❄️"
    if "clear" in desc: return "☀️"
    if "storm" in desc or "thunder" in desc: return "🌩"
    if "mist" in desc or "fog" in desc: return "🌫"
    return "🌡️"

def display_current_weather(data, unit: str):
    if not data: return
    city = data.get("name")
    country = data.get("sys", {}).get("country")
    weather = data.get("weather", [{}])[0].get("description", "N/A").title()
    temp = data.get("main", {}).get("temp", "N/A")
    feels_like = data.get("main", {}).get("feels_like", "N/A")
    humidity = data.get("main", {}).get("humidity", "N/A")
    wind_speed = data.get("wind", {}).get("speed", "N/A")
    unit_symbol = "°C" if unit == "metric" else "°F"
    wind_unit = "m/s" if unit == "metric" else "mph"

    table = Table(title=f"Weather in {city}, {country}", expand=True)
    table.add_column("Condition", justify="center")
    table.add_column("Temperature", justify="center")
    table.add_column("Feels Like", justify="center")
    table.add_column("Humidity", justify="center")
    table.add_column("Wind Speed", justify="center")

    table.add_row(
        f"{weather} {weather_emoji(weather)}",
        f"{temp} {unit_symbol}",
        f"{feels_like} {unit_symbol}",
        f"{humidity}%",
        f"{wind_speed} {wind_unit}"
    )
    console.print(table)

def display_forecast(data, unit: str):
    if not data: return
    unit_symbol = "°C" if unit == "metric" else "°F"
    forecast_list = data.get("list", [])
    table = Table(title=f"5-Day Forecast for {data.get('city', {}).get('name', 'N/A')}", expand=True)
    table.add_column("Date/Time", justify="center")
    table.add_column("Weather", justify="center")
    table.add_column("Temp", justify="center")
    table.add_column("Feels Like", justify="center")
    table.add_column("Humidity", justify="center")
    for entry in forecast_list[::8]:
        dt_txt = entry.get("dt_txt", "N/A")
        weather = entry.get("weather", [{}])[0].get("description", "N/A").title()
        temp = entry.get("main", {}).get("temp", "N/A")
        feels_like = entry.get("main", {}).get("feels_like", "N/A")
        humidity = entry.get("main", {}).get("humidity", "N/A")
        table.add_row(dt_txt, f"{weather} {weather_emoji(weather)}", f"{temp} {unit_symbol}", f"{feels_like} {unit_symbol}", f"{humidity}%")
    console.print(table)

# ------------------------
# Main Program
# ------------------------
def main():
    console.print(Panel.fit("[bold cyan]Welcome to Elite Weather CLI App[/bold cyan]"))
    city = console.input("Enter city name: ").strip()
    unit_choice = console.input("Choose units - (C)elsius or (F)ahrenheit [C]: ").strip().lower()
    unit = "metric" if unit_choice in ["c", ""] else "imperial"
    show_forecast = console.input("Show 5-day forecast? (y/n) [n]: ").strip().lower() == "y"

    for _ in range(10): pass  # simple progress simulation
    weather_data = get_weather(city, unit)
    display_current_weather(weather_data, unit)
    if show_forecast:
        forecast_data = get_forecast(city, unit)
        display_forecast(forecast_data, unit)

if __name__ == "__main__":
    main()
