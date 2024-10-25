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

