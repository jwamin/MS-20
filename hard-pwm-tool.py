#!/usr/bin/python3

from rpi_hardware_pwm import HardwarePWM
from time import sleep
from sys import argv

def uline_print(str:str, character:chr = "="):
    length = len(str)
    print(f"{str}\n{character*length}")

try:
    print("\n")
    uline_print("Hardware PWM Test Tool")
    print("Pins are configured in /boot/config.txt on your RPi")

    print("channel 0, pin 0, chip 0")
    print("keyboard interrupt with Ctrl-C to stop Pulse")
    default_freq = 50 #hz
    default_duty = 50 #square wave
    cycle = False

    #print(argv)
    
    freq:float = float(argv[1]) if len(argv) > 1 else default_freq
    duty:float = float(argv[2]) if len(argv) > 2 else default_duty
    cycle: bool = bool(argv[3]) if len(argv) > 3 else cycle

    print(f"freq: {freq}, duty: {duty}")
    #print(f"freq type: {type(freq)}")

    pwm = HardwarePWM(pwm_channel=0, hz=freq, chip=0)
    pwm.start(duty) # full duty cycle

    current_duty = 0
    fps_60:float = 1 / 120
    total = 100
    step = total * fps_60
    rising = True
    if cycle:
        while(True):
            pwm.change_duty_cycle(current_duty)
            sleep(fps_60)
            if rising:
                current_duty = min(current_duty + step,100)
            else:
                current_duty = max(current_duty - step,0)
            
            if current_duty >= 100 and rising:
                rising = False
            elif current_duty <= 0 and not rising:
                rising = True
    else:
        while(True):
            sleep(1)
except KeyboardInterrupt as kbi:
    print("\n")
    pwm.stop()
