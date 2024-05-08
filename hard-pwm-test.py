from rpi_hardware_pwm import HardwarePWM
from time import sleep
from sys import argv


try:

    default_freq = 60
    default_duty = 10
    
    print(argv)
    
    freq:float = float(argv[1]) if len(argv) > 1 else default_freq
    duty:float = float(argv[2]) if len(argv) > 2 else default_duty
    

    print(f"freq: {freq}, duty: {duty}")
    print(f"freq type: {type(freq)}")

    pwm = HardwarePWM(pwm_channel=0, hz=freq, chip=0)
    pwm.start(duty) # full duty cycle



    #pwm.change_duty_cycle(50)
    #pwm.change_frequency(60)
    while(True):
        sleep(1)
except KeyboardInterrupt as kbi:
    pwm.stop()
