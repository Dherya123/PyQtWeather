# 🌤️ PyQt Weather App

A modern desktop weather application built with Python and PyQt5 that fetches real-time weather information using the OpenWeatherMap API.

## ✨ Features

- 🌍 Search weather by city name
- 🌡️ Displays current temperature in Celsius
- ☀️ Dynamic weather emoji based on weather conditions
- 📝 Weather description (e.g., Clear Sky, Rain, Clouds)
- ⚠️ Handles API and network errors gracefully
- 🎨 Modern PyQt5 user interface

## 🛠️ Technologies Used

- Python
- PyQt5
- Requests
- OpenWeatherMap API

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Dherya123/PyQtWeather.git
```

### 2. Navigate to the project

```bash
cd PyQtWeather
```

### 3. Create a virtual environment

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python main.py
```

## 🔑 OpenWeatherMap API Key

This project uses the OpenWeatherMap API.

1. Create a free account at:
   https://openweathermap.org/

2. Generate your API key.

3. Replace:

```python
api_key = "YOUR_API_KEY"
```

with your own API key.

## 📋 Error Handling

The application handles:

- Invalid city names
- Invalid API key
- Internet connection errors
- Request timeouts
- Server errors
- HTTP exceptions