import board
import neopixel
from math import sin, pi
from matts_leds import repeating_sequence

PIXEL_COUNT = 100
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, brightness=0.5, pixel_order=ORDER, auto_write=False)

wait_times = [(sin(x*1.5*pi/57) + 2) / 40 for x in range(57)]
rgb_values = [(0, 255, 0) for x in range(25)]
rgb_values[0:7] = [(64, 192, 0), (128, 128, 0), (192, 64, 0), (255, 0, 0), (192, 64, 0), (128, 128, 0), (64, 192, 0)]
rgb_values *= 4
repeating_sequence(pixels, PIXEL_COUNT, rgb_values, wait_times)
