import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your OpenWeatherMap API Key
API_KEY = 'your_api_key_here'

def fetch_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

def plot_weather(data, city):
    dates = []
    temps = []

    for entry in data['list']:
        dates.append(entry['dt_txt'])
        temps.append(entry['main']['temp'])

    plt.figure(figsize=(15, 6))
    sns.lineplot(x=dates, y=temps, marker="o")
    plt.title(f"5-Day Temperature Forecast for {city}")
    plt.xticks(rotation=45)
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    city = input("Enter the city name: ")
    weather_data = fetch_weather_data(city)
    if weather_data.get('cod') != "200":
        print("Error:", weather_data.get('message'))
    else:
        plot_weather(weather_data, city)

if __name__ == "__main__":
    main()
