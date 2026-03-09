# Elite Weather CLI App

Get real-time weather information and optional 5-day forecasts for any city, directly from your terminal! 🌤️


---


## Features

- Fetch **current weather** for any city worldwide.
- Optional **5-day forecast** with temperature, humidity, and conditions.
- Supports **Celsius (°C)** and **Fahrenheit (°F)** units.
- Visually appealing **terminal tables** with **weather emojis**.
- Fully interactive **CLI experience** with prompts and progress simulation.
- Clean separation of **API key** in `config.py`.


---


## Demo

$ python weather_cli.py

Enter city name: London

Choose units - (C)elsius or (F)ahrenheit [C]: C

Show 5-day forecast? (y/n) [n]: y


---


### Displays:

- Current weather in a table
- Optional 5-day forecast in another table
- Weather icons for easy visualization


---


## Setup

1. Clone the repository:

```bash
git clone https://github.com/MrV3nomous/weather-cli.git
cd weather-cli
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Add your OpenWeatherMap API key:
• Open config.py
• Replace YOUR_API_KEY = "" with your key: YOUR_API_KEY = "your_real_api_key_here"


####⚠️ Important: Do not push your API key to public repositories.


---


## Usage

Run the program:

```bash
python weather_cli.py
```

Follow the interactive prompts:
- Enter city name
- Choose units (Celsius/Fahrenheit)
- Choose whether to see the 5-day forecast

#### The program will fetch and display weather information in your terminal.


---


## Dependencies
requests
rich


---


### Install all dependencies with:

```bash
pip install -r requirements.txt
```


---


## Notes

• Ensure your OpenWeatherMap API key is active.
• For security, keep your API key private.
• Works on Windows, macOS, and Linux terminals.


---


## License
This project is licensed under the MIT License.

---
