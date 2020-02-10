#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color)
from pybricks.tools import print, wait, StopWatch

#подключение библиотеки
from htcolor_sensor import *

#инициализация датчика
sensor = HTColorSensor(Port.S4)

while True:
    #считывание значений RGB
    red, green, blue = sensor.rgb()

    #считывание цвета
    cur_color = sensor.color()

    print(red, green, blue, cur_color)
    #print(f"Red = {red}, Green = {green}, Blue = {blue}, Cur_color = {cur_color}")
    wait(5)



