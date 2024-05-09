#!/usr/bin/python3

from rpi_hardware_pwm import HardwarePWM
from time import sleep
from sys import argv

PWM_CHANNEL = 0
PWM_CHIP = 0
PWM_FREQUENCY = 100 #hz
PWM_DUTY = 50 #square pulse

def uline_print(str:str, character:chr = "="):
    length = len(str)
    print(f"{str}\n{character*length}")

try:
    print("\n")
    uline_print("Hardware PWM Test Tool")
    print("Pins are configured in /boot/config.txt on your RPi")

    print(f"channel {PWM_CHANNEL}, pin 13, chip {PWM_CHIP}")
    print("Keyboard interrupt with Ctrl-C to stop Pulse")
    default_freq = PWM_FREQUENCY 
    default_duty = PWM_DUTY
    cycle = None
    rise_and_fall = False

    #print(argv)
    
    freq:float = float(argv[1]) if len(argv) > 1 else default_freq
    duty:float = float(argv[2]) if len(argv) > 2 else default_duty
    cycle:float = float(argv[3]) if len(argv) > 3 else cycle
    rise_and_fall = bool(argv[4]) if len(argv) > 4 else rise_and_fall

    print(f"freq: {freq}, initial duty: {duty} cycle: {cycle} rise_and fall: {rise_and_fall}")
    #print(f"freq type: {type(freq)}")

    pwm = HardwarePWM(pwm_channel=PWM_CHANNEL, hz=freq, chip=PWM_CHIP)
    pwm.start(duty) # full duty cycle


    if cycle:
        duty_min = 0.1
        duty_max = 100
        current_duty = duty_min
        cycle_freq = cycle 
        step = cycle_freq / freq
        rising = rise_and_fall
        cycle_step = 1 / cycle_freq
        print(f"cycle freq: {cycle_freq}, step: {step}, cycle_step: {cycle_step}")
        while(True):
            pwm.change_duty_cycle(current_duty)
            sleep(cycle_step)
            #print(current_duty)
            if rise_and_fall:
                if rising:
                    current_duty = min(current_duty + step,duty_max)
                else:
                    current_duty = max(current_duty - step,duty_min)
                if rise_and_fall:
                    if current_duty >= duty_max and rising:
                        rising = False
                    elif current_duty <= duty_min and not rising:
                        rising = True
            else:
                current_duty = min(current_duty + step, duty_max) if current_duty < duty_max else 0 
    else:
        while(True):
            sleep(1)
except KeyboardInterrupt as kbi:
    print("\n")
    pwm.stop()
