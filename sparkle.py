import board
import neopixel
import random
import time

PIXEL_COUNT = 100
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, brightness=0.75, pixel_order=ORDER, auto_write=False)
DEFAULT = (32, 32, 64)
SPARKLE = (242, 236, 177)
DIM_SPARKLE = (120, 120, 120)
DYING_SPARKLE = (60, 60, 90)

pixels.fill(DEFAULT)
pixels.show()

while True:
    sparkles = random.randint(2, 6)
    sources = [random.randint(int(PIXEL_COUNT*sparkle/sparkles) + 2,int(PIXEL_COUNT*(sparkle+1)/sparkles) - 3) for sparkle in range(sparkles)]

    for source in sources:
        pixels[source] = SPARKLE
        pixels.show()
    time.sleep(0.05)
    
    for source in sources:
        pixels[source-1] = DIM_SPARKLE
        pixels[source] = DIM_SPARKLE
        pixels[source+1] = DIM_SPARKLE
        pixels.show()
    time.sleep(0.05)

    for source in sources:
        pixels[source-2] = DYING_SPARKLE
        pixels[source-1] = DYING_SPARKLE
        pixels[source] = DYING_SPARKLE
        pixels[source+1] = DYING_SPARKLE
        pixels[source+2] = DYING_SPARKLE
        pixels.show()
    time.sleep(0.05)

    pixels.fill(DEFAULT)
    pixels.show()
    time.sleep(random.randint(3,30)/100)



