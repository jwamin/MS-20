import RPi.GPIO as GPIO
from time import sleep
from typing import List

GPIO.setmode(GPIO.BOARD)

def pinTest(pin,duration:int = 1):
    GPIO.output(pin, GPIO.HIGH)
    print(f"pin {pin} going LOW")
    sleep(duration)
    GPIO.output(pin,GPIO.LOW)


def testRoutine(chan_list:List[int],parallel: bool):

    #for pin in chan_list:
    GPIO.setup(chan_list,GPIO.OUT)

    if parallel:
        print(f"pins {chan_list} going HIGH") 
        GPIO.output(chan_list, GPIO.HIGH)

    for pin in chan_list:
        pinTest(pin)


pins = [11,32,37]

for parallel in [True,False]:
    testRoutine(pins,parallel)
    sleep(0.5)

print("DONE, cleaning up...")

GPIO.cleanup()
