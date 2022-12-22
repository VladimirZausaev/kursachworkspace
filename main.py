import numpy as np
import requests
from bokeh.plotting import figure, show
from typing import List
from datetime import datetime, date


def get_temp(own_city_name: str) -> List:
    api = "https://api.openweathermap.org/data/2.5/forecast?q=" + own_city_name + "&APPID=d438c29584f3e371f54cc81a6529daaf"

    json_data = requests.get(api).json()
    temp = []
    for i in json_data['list']:
        temp.append(float(i['main']['temp'])-273)

    return temp


def get_date(own_city_name: str) -> List:
    api = "https://api.openweathermap.org/data/2.5/forecast?q=" + own_city_name + "&APPID=d438c29584f3e371f54cc81a6529daaf"

    json_data = requests.get(api).json()

    date = []

    for i in json_data['list']:
        data = i['dt_txt'].split(" ")
        time = data[1].split(":")
        data = data[0].split("-")
        date.append(int(data[2]) + int(time[0])/24)

    return date


a = input('Введите город: ')


y = list((get_temp(a)))
x = list((get_date(a)))

x_new = []
y_new = []

for i in range(0, len(y) - 1, 6):
    y_new.append(y[i])
    x_new.append(x[i])

plot = figure(
    title=f'Погода: {a}',
    x_axis_label='Дата',
    y_axis_label='Температура'
)
plot.dot(x_new, y_new, size=45, color='red')
plot.line(x, y, line_width=1.5)
show(plot)



