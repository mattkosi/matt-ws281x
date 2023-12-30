#!/bin/bash

PID=$(sudo ps x | grep "sudo python3" | awk -F ' ' '{print $1}')
if [ ! $PID ]; then
  echo "Unable to find python3 script running"
  exit 1
fi

KILL_PROCESS=$(sudo kill $PID)
if [ $KILL_PROCESS ]; then
  echo "There was a problem killing process $PID"
  exit 1
fi

CLEAR_LEDS=$(sudo python3 $(pwd)/turn_off_leds.py)
if [ $CLEAR_LEDS ]; then
  echo "Unable to turn off the LEDs"
  exit 1
fi

echo "Your LEDs have been turned off"
exit 0
