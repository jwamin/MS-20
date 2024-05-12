from common import pulse_frequency_mod_easing, uline_print, Easing, PWM_FREQUENCY, PWM_DEFAULT_MOD_FREQUENCY
#from pitchtools import
from sys import argv
uline_print("pulse fm easing test tool")

# note1:float = str(argv[1]) if len(argv) > 1 else PWM_FREQUENCY
# mod_freq:float = float(argv[2]) if len(argv) > 2 else PWM_DEFAULT_MOD_FREQUENCY
# functionString: str = str(argv[3]) if len(argv) > 3 else Easing.linear.name
# print(argv)
# easing_function = Easing[functionString].value

pulse_frequency_mod_easing()