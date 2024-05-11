from rpi_hardware_pwm import HardwarePWM
from easing_functions import *
from time import sleep
from sys import argv
from typing import Callable

PWM_CHANNEL = 0
PWM_CHIP = 0
PWM_FREQUENCY = 100 #hz
PWM_DUTY = 50 #square pulse
PWM_DEFAULT_TRANSITION_TIME = 2 #seconds

FPS_60 = 1 / 60

def uline_print(str:str, character:chr = "="):
    length = len(str)
    print(f"{str}\n{character*length}")


def start_pwm(freq:float, duty: float, cycle: bool, rise_and_fall: bool):
    try: 
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

def pwm_easing(easingFunction:Callable = QuinticEaseInOut,frequency:float = PWM_FREQUENCY,time:int=PWM_DEFAULT_TRANSITION_TIME):

    try:
        pwm = HardwarePWM(pwm_channel=PWM_CHANNEL, hz=frequency, chip=PWM_CHIP)
        pwm.start(0) # full duty cycle

        ease = easingFunction(0,100,time)
        complete = FPS_60 * 60 * 2
        current = 0

        print(f"starting easing pwm with{easingFunction}")
        print(f"frequency: {frequency}, cycle duration: {time} seconds")
        while(True):
            while current <= complete:
                newduty = ease(current)
                pwm.change_duty_cycle(newduty)
                current = current + FPS_60
                sleep(FPS_60)
            current = 0
    except KeyboardInterrupt as kbi:
        print("\n")
        pwm.stop()