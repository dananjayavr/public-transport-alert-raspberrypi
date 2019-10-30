import requests
import json

from time import sleep

def get_tram_status():
    r = requests.get('https://api-ratp.pierre-grimaud.fr/v4/traffic/tramways/2')
    response = json.loads(r.text)

    if('normal' in response['result']['slug']):
        return 'normal'
    else:
        return 'interrupted'

def get_next_trams():
    try:
        r = requests.get('https://api-ratp.pierre-grimaud.fr/v4/schedules/tramways/2/Suresnes+Longchamp/A')
        response = json.loads(r.text)
        next_trams = []
        for time in response['result']['schedules']:
            if time == 'A l\'arret':
                next_trams[0] = 0
                next_trams[1] = time['message'][1].strip(' mn')
            elif time == 'A l\'approche':
                next_trams[0] = 0
                next_trams[1] = time['message'][1].strip(' mn')
            else:
                next_trams.append(time['message'].strip(' mn'))
        
        return next_trams
    except KeyError:
        sleep(5)
        get_next_trams() 

# TODO : Complete the algorithm
""" def calculate_time_to_leave():
    next_trams = get_next_trams()
    walking_time = 8 
    times = []
    for time in next_trams:
        times.append(time)
    
    if(int(next_trams[0]) - int(walking_time > 0)):
        if((int(next_trams[0]) - int(walking_time)) >= 2):
            return 'Leave now'
        else:
            return (int(next_trams[1]) - int(walking_time))  
    else:
        return (int(next_trams[1]) - int(walking_time))
           """