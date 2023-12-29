import board
import neopixel
import colorsys
from matts_leds import repeating_sequence
from time import sleep

PIXEL_COUNT = 100
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, brightness=0.5, pixel_order=ORDER, auto_write=False)

while True:
    for x in range(PIXEL_COUNT):
        pixels[x] = (255, 255, 255)
        pixels.show()
        sleep(0.01)
    sleep(.25)
    for x in range(PIXEL_COUNT):
        pixels[x] = (0, 255, 0)
        pixels.show()
        sleep(0.01)
    sleep(.25)
    for x in range(PIXEL_COUNT):
        pixels[x] = (255, 0, 0)
        pixels.show()
        sleep(0.01)
    sleep(.25)
