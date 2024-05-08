from rpi_hardware_pwm import HardwarePWM
from time import sleep

pwm = HardwarePWM(pwm_channel=0, hz=100, chip=0)

try: 
    pwm.start(50) # full duty cycle
    
    sleep(10)
    
    pwm.change_duty_cycle(30)

    sleep(10)

    pwm.change_frequency(200)
    pwm.change_duty_cycle(1)

    ind = 0
    duty = 0
    while(True):
        print(f"duty now {duty}")
        pwm.change_duty_cycle(duty)
        duty = 0 if duty >= 100 else duty + 1
        if duty % 5 == 0: 
            print(f"duty now {duty}")
        sleep(0.01)
    
except KeyboardInterrupt as kbi:
    print(f"my keyboard interrupt {kbi}")
    pwm.stop()

