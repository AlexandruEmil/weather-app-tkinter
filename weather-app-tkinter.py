import requests
import tkinter as tk
from tkinter import messagebox

# API Key for OpenWeatherMap
API_KEY = 'YOUR_API_KEY_HERE' 
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
ONE_CALL_URL = 'https://api.openweathermap.org/data/2.5/onecall'

def get_weather():
    city = city_entry.get()
    if city:
  
        url = f"{WEATHER_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            humidity = main['humidity']
            weather = data['weather'][0]['description']
            lat = data['coord']['lat']
            lon = data['coord']['lon']
            
            result = f"Temperature: {temperature}°C\nHumidity: {humidity}%\nConditions: {weather.capitalize()}"
            result_label.config(text=result)

            forecast_url = f"{ONE_CALL_URL}?lat={lat}&lon={lon}&exclude=current,minutely,hourly&appid={API_KEY}&units=metric"
            forecast_response = requests.get(forecast_url)
            if forecast_response.status_code == 200:
                forecast_data = forecast_response.json()
             
                forecast_text = "Extended Forecast:\n"
                for day in forecast_data['daily'][:5]:  # 5 days
                    temp_day = day['temp']['day']
                    temp_night = day['temp']['night']
                    weather_desc = day['weather'][0]['description']
                    forecast_text += f"Day: {temp_day}°C, Night: {temp_night}°C, {weather_desc.capitalize()}\n"
                
        
                if 'alerts' in forecast_data:
                    alerts = forecast_data['alerts']
                    alert_text = "Weather Alerts:\n"
                    for alert in alerts:
                        event = alert['event']
                        description = alert['description']
                        alert_text += f"{event}: {description}\n"
                else:
                    alert_text = "No weather alerts."

            
                result_label.config(text=result + "\n\n" + forecast_text + "\n" + alert_text)
            else:
                messagebox.showerror("Error", "Unable to fetch extended forecast.")
        else:
            messagebox.showerror("Error", "City not found.")
    else:
        messagebox.showwarning("Warning", "Please enter a city name!")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")


city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack(pady=5)


get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 10))
result_label.pack(pady=20)


root.mainloop()
