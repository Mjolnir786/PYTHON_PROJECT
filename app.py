from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "6fddfce7fc11a0d95c323b1b9ba031e0"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    
    if response.get("cod") != 200:
        return render_template('error.html', message=response.get("message", "City not found"))

    weather_data = {
        "city": response["name"],
        "temperature": response["main"]["temp"],
        "description": response["weather"][0]["description"],
        "icon": response["weather"][0]["icon"],
        "humidity": response["main"]["humidity"],
        "wind_speed": response["wind"]["speed"],
    }
    return render_template('result.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
