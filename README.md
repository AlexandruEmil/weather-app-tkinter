# weather-app-tkinter
This program is a weather application that fetches weather information from an API and displays it using a Tkinter-based graphical user interface (GUI). It allows users to search for weather information of a specific location by entering the city name.

# Dependencies:
Python 3.x
Tkinter library
JSON module
Requests module

# File Structure:
weather_app.py: The main Python script that contains the application logic and GUI components.

#Functionality:
#GUI Design:

The program uses Tkinter to create a simple and intuitive graphical interface.
It includes a text entry field for users to enter the city name.
A search button triggers the API request to fetch weather data.
Weather information is displayed in a visually appealing format.
#API Integration:
The program utilizes the Requests module to send HTTP requests to an external weather API.
It fetches weather data in JSON format.

#Weather Data Display:

The JSON response from the API is parsed using the JSON module to extract relevant weather information.
The program displays the fetched data, including current temperature, weather description, humidity, wind speed, etc.
Error Handling:

The program handles potential errors, such as invalid input, network issues, or unavailable API responses.
Error messages are displayed to guide the user and ensure smooth program execution.
#Usage:
Run the weather_app.py script using Python 3.x.
Enter the name of the city for which you want to check the weather.
Click the "Search" button.
The program will fetch weather data from the API and display it on the GUI.

#Note:
You need an internet connection for the program to access the weather API.
Ensure that all dependencies are installed before running the script.

#UPDATE:
 Improvements and Extension:
 Extended Forecasts uses the One Call API from OpenWeatherMap to add multi-day forecasts. This can display the weather for the next few days, including temperature highs and lows, and conditions.
 Weather Alerts: If available for the selected location, display any active weather alerts (such as severe storms or heavy rainfall warnings) by querying the One Call API, which includes alerts for certain regions.
 Enhanced Error Handling(idk,why it wasn't on the start :( ): 
 Improve the clarity of error messages by detailing specific issues, such as:
 -Invalid city name: Inform the user if the city isn’t recognized.
 -Network issues: Notify if there’s a connection error.
 -Invalid API key: Remind the user to check if the API key is correctly set.
 
