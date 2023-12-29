from time import sleep

# led_values is the pre-drawn list of colors. The length may differ from pixel_count.
# sleep_times can be a float or a list of values of any length.

def _next_sleep(sleep_is_list, sleep_times, sleep_index):
    if sleep_is_list:
        sleep(sleep_times[sleep_index])
        next_sleep_index = 0 if (sleep_index+1==len(sleep_times)) else (sleep_index+1)
        return next_sleep_index
    else:
        sleep(sleep_times)
        return None

def repeating_sequence(pixels, pixel_count, led_values, sleep_times):
    sleep_index = 0
    i = 0
    led_index = 0
    led_values_count = len(led_values)
    sleep_is_list = isinstance(sleep_times, list)
    
    if pixel_count == led_values_count:
        while True:
            while (i<pixel_count):
                pixels[i] = led_values[led_index]
                i, led_index = i+1, led_index+1
                led_index = 0 if (led_index==led_values_count) else led_index
            pixels.show()
            sleep_index = _next_sleep(sleep_is_list, sleep_times, sleep_index)
            i = 0
            led_index = ((led_index+1) % led_values_count)
    
    elif pixel_count > led_values_count:
        new_led_values = led_values*(pixel_count//led_values_count) + led_values[:pixel_count%led_values_count]
        while True:
            while (i<pixel_count):
                pixels[i] = new_led_values[led_index]
                i, led_index = i+1, led_index+1
                led_index = 0 if (led_index==led_values_count) else led_index
            pixels.show()
            sleep_index = _next_sleep(sleep_is_list, sleep_times, sleep_index)
            i = 0
            led_index = ((led_index+1) % led_values_count)
    
    elif pixel_count < led_values_count:
        while True:
            initial_led_index = led_index
            while (i<pixel_count):
                pixels[i] = led_values[led_index]
                i, led_index = i+1, led_index+1
                if led_index == led_values_count:
                    led_index = 0
            pixels.show()
            sleep_index = _next_sleep(sleep_is_list, sleep_times, sleep_index)
            i = 0
            led_index = ((initial_led_index+1) % led_values_count)

def repeating_sequence_all_pixels(pixels, led_values, sleep_times):
    sleep_index = 0
    led_index = 0
    led_values_count = len(led_values)
    sleep_is_list = isinstance(sleep_times, list)

    while True:
        pixels.fill(led_values[led_index])
        pixels.show()
        sleep_index = _next_sleep(sleep_is_list, sleep_times, sleep_index)
        led_index = ((led_index+1) % led_values_count)