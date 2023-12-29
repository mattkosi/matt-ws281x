import board
import neopixel
import colorsys
from matts_leds import repeating_sequence

PIXEL_COUNT = 100
ORDER = neopixel.RGB
BUCKETS = 1
HUE_MAX = 360
pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, brightness=0.5, pixel_order=ORDER, auto_write=False)

rgb_values = [colorsys.hsv_to_rgb((x*BUCKETS*(HUE_MAX/PIXEL_COUNT/2)%HUE_MAX)/HUE_MAX,.85,1) for x in range(PIXEL_COUNT*2)]
rgb_values = [(int(value[0]*255), int(value[1]*255), int(value[2]*255)) for value in rgb_values]
repeating_sequence(pixels, PIXEL_COUNT, rgb_values, .02)
