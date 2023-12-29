import board
import neopixel
import colorsys
from time import sleep
from matts_leds import repeating_sequence

PIXEL_COUNT = 100
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, brightness=0.33, pixel_order=ORDER, auto_write=False)
steps = 100

colors = [(255,0,0), (255,30,0), (128,128,0), (0,255,0), (0,128,128), (0,0,255), (128,0,128)]
rgb_values = []
for (r,g,b) in colors:
    rgb_values += [(int(r*x/steps), int(g*x/steps), int(b*x/steps)) for x in range(steps)]
    rgb_values += [(int(r*x/steps), int(g*x/steps), int(b*x/steps)) for x in range(steps-1, -1, -1)]
    rgb_values += [(0,0,0) for x in range(int(steps/2))]

repeating_sequence(pixels, PIXEL_COUNT, rgb_values, .01)
