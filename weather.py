import json
from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests

url_api = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_file = 'API.Key'
file_a = ConfigParser()
file_a.read(api_file)
api_key = file_a['api_key']['key']


def weather_find(city):
    final = requests.get(url_api.format(city,api_key))
    if final:
        json_file = final.json()
        city = json_file['name'] #with reference to api site used
        country_name = json_file['sys']['country'] #with reference to api site used
        k_temperature = json_file['main']['temp'] #with reference to api site used
        c_temperature = k_temperature - 273.15
        #f_temperature = (k_temperature-273.15)*9/5+32
        weather_display = json_file['weather'][0]['main'] #with reference to api site used
        result = (city,country_name,k_temperature,c_temperature,weather_display)

        return result
    else:
        return None

def print_weather():
    city = search_city.get()
    weather = weather_find(city) #Previous function variable
    if weather:
        location_entry['text'] = '{}, {}'.format(weather[0],weather[1])
        temperature_entry['text'] = '{:.2f} F, {:.2f} C'.format(weather[2], weather[3])
        weather_entry['text'] = weather[4]

    else:
        messagebox.showerror('Error','Please enter a valid city name')



app = Tk() #tkinter window
app.title("Weather App")
app.config(background="grey")
app.geometry("700x400")

search_city = StringVar()
enter_city = Entry(app, textvariable=search_city, fg="Black", bg="white" , font=("Arial",30,"bold")) #bydefault bg="white" (fg here is font color)
enter_city.pack()  #pack() allows to put all above things(citybox) to tkinter window

search_button = Button(app, text='SEARCH WEATHER!' ,width=20, bg="Blue", fg="white", font=("Arial",25,"bold"),command=print_weather)
search_button.pack()

location_entry = Label(app, text='', font=("Arial", 35,"bold") ,bg="lightblue")
location_entry.pack()

temperature_entry = Label(app, text='', font=("Arial",35,"bold"),bg="lightpink")
temperature_entry.pack()

weather_entry= Label(app, text='', font=("Arial",35,"bold"),bg="lightblue")
weather_entry.pack()


app.mainloop()