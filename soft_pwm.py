import RPi.GPIO as GPIO
from time import sleep
from typing import List
from gpiozero import PWMOutputDevice

def pinTest(pin,duration:int = 1):
    GPIO.output(pin, GPIO.HIGH)
    print(f"pin {pin} going LOW")
    sleep(duration)
    GPIO.output(pin,GPIO.LOW)


def testRoutine(chan_list:List[int],parallel: bool):
    GPIO.setmode(GPIO.BOARD)
    #for pin in chan_list:
    GPIO.setup(chan_list,GPIO.OUT)

    if parallel:
        print(f"pins {chan_list} going HIGH") 
        GPIO.output(chan_list, GPIO.HIGH)

    for pin in chan_list:
        pinTest(pin)
    GPIO.cleanup()

pins = [32]

pwm_pin_number = 12

pwm_device = PWMOutputDevice(pwm_pin_number,active_high=False,frequency=100)

pwm_device.pulse(fade_in_time=0,fade_out_time=0)

sleep(7)
for freq in [100,200,300,400,500]:
    pwm_device.frequency = freq*3
    sleep(3)

#sleep(7)

pwm_device.on()

pwm_device.close()





