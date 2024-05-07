from rpi_hardware_pwm import HardwarePWM
from time import sleep

pwm = HardwarePWM(pwm_channel=0, hz=100, chip=0)
pwm.start(100) # full duty cycle

pwm.change_duty_cycle(50)

sleep(10)

pwm.change_frequency(200)

sleep(10)

pwm.stop()
