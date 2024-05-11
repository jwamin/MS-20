#!/usr/bin/python3
from sys import argv
from common import uline_print, start_pwm, PWM_CHANNEL, PWM_CHIP, PWM_DEFAULT_DUTY,PWM_FREQUENCY

print("\n")
uline_print("Hardware PWM Test Tool")
print("Pins are configured in /boot/config.txt on your RPi")

print(f"channel {PWM_CHANNEL}, pin 13, chip {PWM_CHIP}")
print("Keyboard interrupt with Ctrl-C to stop Pulse")
default_freq = PWM_FREQUENCY 
default_duty = PWM_DEFAULT_DUTY
cycle = None
rise_and_fall = False

#print(argv)

freq:float = float(argv[1]) if len(argv) > 1 else default_freq
duty:float = float(argv[2]) if len(argv) > 2 else default_duty
cycle:float = float(argv[3]) if len(argv) > 3 else cycle
rise_and_fall = bool(argv[4]) if len(argv) > 4 else rise_and_fall

print(f"freq: {freq}, initial duty: {duty} cycle: {cycle} rise_and fall: {rise_and_fall}")

start_pwm(freq,duty,cycle,rise_and_fall)


