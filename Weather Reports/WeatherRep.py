#Import Modules
import requests #pip install requests
import datetime #pip install datetime
#Api Key
api_key = '57cc670244756600bc88e10ac0be835d'

user_input = input("Enter City: ")  #Get the city to get Weather details

#Get The Weather Details from openweathermap
weather_data = requests.get(

    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")


#Get Date And Time
e = datetime.datetime.now()

print ("\nToday's date: = %s/%s/%s" % (e.day, e.month, e.year))

     #Error Handling
if weather_data.json()['cod'] == '404':
    print("\nNo City Found")
#Print the weather
else:

    weather = weather_data.json() ['weather'] [0] ['main'] 
    temp = weather_data.json() ['main'] ['temp']
    feels_like = weather_data.json() ['main'] ['feels_like']
    humidity = weather_data.json() ['main'] ['humidity']
    visibility = weather_data.json() ['visibility']
    wind = weather_data.json() ['wind']
    

    print(f"\nThe weather in {user_input} is: {weather}")
    print(f"\nThe temperature in {user_input} is: {temp} F and feels like {feels_like} F")
    print(f"\nThe humadity in {user_input} is: {humidity}%")
    print(f"\nThe visibility in {user_input} is: {visibility}")
    print(f"\nThe wind speed in {user_input} is: {wind}")