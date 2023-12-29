import board
import neopixel
import colorsys

PIXEL_COUNT = 100
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, brightness=0.5, pixel_order=ORDER, auto_write=False)

pixels.fill((0,0,0)) 
pixels.show()
