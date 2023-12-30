import board
import neopixel
import colorsys
from time import sleep
from random import choice

PIXEL_COUNT = 100
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(board.D18, PIXEL_COUNT, brightness=0.3, pixel_order=ORDER, auto_write=False)

pixels.fill((0,0,0))
while True:
    forwards = True
    start = 0
    end = PIXEL_COUNT-1
    current = 0
    sleep_length = 0.02
    colors = [(255,0,0),(255,30,0),(128,128,0),(0,255,0),(0,128,128),(0,0,255),(128,0,128)]
    color = choice(colors)
    while ((end-start)!=1):
        pixels[current] = color
        if forwards:
            if (current != start):
                pixels[current-1] = (64,64,64)
            if (current == end):
                forwards = False
                end -= 1
            current = (current+1) if ((current+1) <= end) else current-1
        else:
            if (current != end):
                pixels[current+1] = (64,64,64)
            if (current == start):
                forwards = True
                start += 1
            current = (current-1) if ((current-1) >= start) else current+1
        pixels.show()
        sleep(sleep_length)
    forwards = True
    start = 0
    end = PIXEL_COUNT-1
    current = 0 
    while ((end-start)!=1):
        pixels[current] = (64,64,64)
        if forwards:
            if (current != start):
                pixels[current-1] = color
            if (current == end):
                forwards = False
                end -= 1
            current = (current+1) if ((current+1) <= end) else current-1
        else:
            if (current != end):
                pixels[current+1] = color
            if (current == start):
                forwards = True
                start += 1
            current = (current-1) if ((current-1) >= start) else current+1
        pixels.show()
        sleep(sleep_length)
