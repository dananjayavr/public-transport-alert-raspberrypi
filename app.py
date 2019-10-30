#!/usr/bin/python3

import datetime
from time import sleep
from calculate import get_next_trams
from draw import draw
from sense_hat import SenseHat

sense = SenseHat()

stop_time = datetime.datetime.now() + datetime.timedelta(hours=1)

while datetime.datetime.now() <= stop_time:
    next_trams = get_next_trams()
    walking_time = 8 
    times = []
    try:
        for time in next_trams:
            if(time == "A l'approche"):
                time = 0
            if(time == "A l'arret"):
                time = 0
            times.append(time)
    except TypeError:
        pass

    first = times[0]
    second = times[1]
    
    print(times)
    
    if(len(times) == 2):
        if(int(first) == walking_time):
            draw('yellow')
        elif (int(first) - walking_time == 2 or int(first) - walking_time == 1):
            draw('green')
        else:
            draw('red')
    else:
        draw('warning')
    
    sleep(30)

sense.clear()