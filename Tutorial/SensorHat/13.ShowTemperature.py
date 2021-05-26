import numpy as np
from time import sleep
from sense_emu import SenseHat

def get_scale(value, min_value, max_value, min_pixel=0, max_pixel=8):
    # Range check
    if value < min_value:
        value = min_value
    if max_value < value:
        value = max_value

    value_range = max_value - min_value
    pixel_range = max_pixel - min_pixel
    return (((value - min_value) / value_range) * pixel_range) + min_pixel

def draw_bar(screen, origin, width, height, color):
    # Calculate the coordinates of the boundaries
    x1, y1 = origin
    x2 = x1 + width
    y2 = y1 + height
    # Invert the Y-coords so we're drawing bottom up
    max_y, max_x = screen.shape[:2]
    y1, y2 = max_y - y2, max_y - y1
    # Draw the bar
    screen[y1:y2, x1:x2, :] = color


sh = SenseHat()
while True:
    # Decide each sensor range
    temperature_range = (0, 40)
    pressure_range = (950, 1050)
    humidity_range = (0, 100)
    # Get each sensor value and change LED scale
    temperature = get_scale(sh.temperature, *temperature_range)
    pressure = get_scale(sh.pressure, *pressure_range)
    humidity = get_scale(sh.humidity, *humidity_range)
    # make screen buffer LED Matrix 8(Height) * 8(Width) * 3(Color)
    screen = np.zeros((8, 8, 3), dtype=np.uint8)
    # Draw Bar to screen (3 position(0, 0), (3, 0), (6, 0))
    draw_bar(screen, (0, 0), 2, round(temperature), color=(255, 0, 0))
    draw_bar(screen, (3, 0), 2, round(pressure), color=(0, 255, 0))
    draw_bar(screen, (6, 0), 2, round(humidity), color=(0, 0, 255))
    # Set screen to LED 
    sh.set_pixels([pixel for row in screen for pixel in row])

    sleep(1)
