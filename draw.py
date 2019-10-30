from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.low_light = True
sense.set_rotation(180)

def draw(color):
    X = [0, 181, 155]  # T2 Green
    R = [255, 0, 0]  # Red
    G = [0, 255, 0] # Green
    Y = [255, 255, 0] # Yellow

    if color == 'green':
        shape = [
        X, X, X, X, X, X, X, X,
        X, G, G, G, G, G, G, X,
        X, G, G, G, G, G, G, X,
        X, G, G, G, G, G, G, X,
        X, G, G, G, G, G, G, X,
        X, G, G, G, G, G, G, X,
        X, G, G, G, G, G, G, X,
        X, X, X, X, X, X, X, X
        ]
        sense.set_pixels(shape)
    
    elif color == 'yellow':
        shape = [
        X, X, X, X, X, X, X, X,
        X, Y, Y, Y, Y, Y, Y, X,
        X, Y, Y, Y, Y, Y, Y, X,
        X, Y, Y, Y, Y, Y, Y, X,
        X, Y, Y, Y, Y, Y, Y, X,
        X, Y, Y, Y, Y, Y, Y, X,
        X, Y, Y, Y, Y, Y, Y, X,
        X, X, X, X, X, X, X, X
        ]
        sense.set_pixels(shape)

    elif color == 'warning':
        sense.show_letter('!',back_colour=[255,0,0])

    else:
        shape = [
        X, X, X, X, X, X, X, X,
        X, R, R, R, R, R, R, X,
        X, R, R, R, R, R, R, X,
        X, R, R, R, R, R, R, X,
        X, R, R, R, R, R, R, X,
        X, R, R, R, R, R, R, X,
        X, R, R, R, R, R, R, X,
        X, X, X, X, X, X, X, X
        ]
        sense.set_pixels(shape)