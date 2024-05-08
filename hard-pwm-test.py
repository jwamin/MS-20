from rpi_hardware_pwm import HardwarePWM
from time import sleep
try:
    pwm = HardwarePWM(pwm_channel=0, hz=60, chip=0)
    pwm.start(10) # full duty cycle

    #pwm.change_duty_cycle(50)
    #pwm.change_frequency(60)
    while(True):
        sleep(1)
except KeyboardInterrupt as kbi:
    pwm.stop()
