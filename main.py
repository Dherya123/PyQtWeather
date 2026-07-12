import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.bg = QLabel(self)
        self.pixmap = QPixmap("assets/images/weather_bg.jpg")
        self.bg.lower()

        self.city_label = QLabel("Enter the city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.icon_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.get_weather_button.setFixedSize(300, 70)
        
        self.container = QWidget()

        container_layout = QVBoxLayout()
        container_layout.addWidget(self.city_label)
        container_layout.addWidget(self.city_input)
        container_layout.addWidget(self.get_weather_button, alignment=Qt.AlignCenter)
        container_layout.addWidget(self.temperature_label)
        container_layout.addWidget(self.icon_label)
        container_layout.addWidget(self.description_label)

        self.container.setLayout(container_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.container)
        main_layout.setContentsMargins(450, 70, 450, 70)

        self.setLayout(main_layout)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.container.setObjectName("container")
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.icon_label.setObjectName("icon_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QWidget#container{
                border-radius: 30px;
                background-color: rgb(147, 183, 245, 30);
            }
            QLabel, QPushButton{
                font-family: calibri;
            }
            QLabel#city_label{
                font-size: 40px;
                font-style: italic;
                font-weight: bold;
                color:black;
            }
            QLineEdit#city_input{
                font-size: 50px;
                padding: 1px;
                border-radius: 10px;
                color: black;
                background-color: #e4ebf7;
            }
            QPushButton#get_weather_button{
                font-size: 40px;
                font-weight: bold;
                color: black;
                background-color: white;
                border-radius: 20px;
            }
            QLabel#temperature_label{
                font-size: 75px;
            }
            QLabel#icon_label{
                font-size: 100px;
                font-family: Apple Color Emoji;
            }
            QLabel#description_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
        self.showFullScreen()
    
    def resizeEvent(self, event):
        self.bg.setGeometry(self.rect())
        self.bg.setPixmap(
            self.pixmap.scaled(
                self.size(),
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
        )
        super().resizeEvent(event)

    def get_weather(self):
        api_key = "68d1ca38b57e04dc9224dc189e567aa0"
        city_name = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal server error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")
        
        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        
        self.icon_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        self.temperature_label.setText(f"{temperature_c:.0f}°C")

        weather_id = data["weather"][0]["id"]
        self.icon_label.setText(self.get_weather_icon(weather_id))

        weather_description = data["weather"][0]["description"]
        self.description_label.setText(weather_description)

    @staticmethod
    def get_weather_icon(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""

def main():
    app = QApplication(sys.argv)
    weather = WeatherApp()
    weather.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()