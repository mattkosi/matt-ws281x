import board
import neopixel
import colorsys
from matts_leds import repeating_sequence

PIXEL_COUNT = 100
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, brightness=0.5, pixel_order=ORDER, auto_write=False)

rgb_values = [(255,0,0),(255,255,255),(0,255,0),(255,255,255)]
repeating_sequence(pixels, PIXEL_COUNT, rgb_values, .25)
