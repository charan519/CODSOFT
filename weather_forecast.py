import tkinter as tk
from urllib import request
import json

def get_weather():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    location = location_entry.get()
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    
    with request.urlopen(base_url) as response:
        response_data = response.read()
    
    weather_data = json.loads(response_data)
    
    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]
        description = weather_data["weather"][0]["description"]
        
        result_label.config(
            text=f"Temperature: {temperature}°C\n"
                 f"Humidity: {humidity}%\n"
                 f"Wind Speed: {wind_speed} m/s\n"
                 f"Description: {description.capitalize()}"
        )
    else:
        result_label.config(text="Location not found!")

# Create the main window
root = tk.Tk()
root.title("Weather Forecast App")

# Create input field for location
location_label = tk.Label(root, text="Enter Location:")
location_label.pack(pady=10)

location_entry = tk.Entry(root)
location_entry.pack(pady=5)

# Create get weather button
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Create result label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
