import tkinter as tk
from PIL import ImageTk, Image
import requests
from tkinter import font
height = 500
width = 600
root = tk.Tk()


def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str(name)+ ' ' + str(desc) + ' ' + str(temp)
    except:
        final_str = 'city: {} \n Weather conditions: {}\n Temperature: {}'.format(name,desc,temp)
    
    return final_str
def testFunction(entry):
    print('the entry is:', entry)

def get_weather(city):
    weather_key = 'THIS IS WHERE THE API KEY GOES, BUT I HAD TO HIDE IT ON MY GITHUB :)'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key,'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)

#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

canvas = tk.Canvas(root, height=height, width = width)
canvas.pack()

img = ImageTk.PhotoImage(Image.open("cartoon.jpg"))  
l=tk.Label(root,image=img)
l.place(relwidth=1, relheight=1)


frame = tk.Frame(root,bg='#1EA9B2',bd='5')
frame.place(relx="0.5", rely="0.1",relwidth="0.75", relheight ="0.1", anchor='n')


entry = tk.Entry(frame, font=('Courier',25))
entry.place(relwidth='0.65', relheight='1')

button = tk.Button(frame,text="Get Weather", fg='red', command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relheight='1', relwidth='0.3')

lower_frame = tk.Frame(root, bg='#1EA9B2',bd=10)
lower_frame.place(relwidth='0.75', relx ='0.5', rely='0.25', relheight = '0.6', anchor='n')

label = tk.Label(lower_frame, bg='#FFA07A', font=('Courier',13))
label.place( relwidth='1', relheight='1')

root.mainloop()
