# Replace sence_emu with sence_hat for use with physical HAT

from sense_emu import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()

sense.show_message("Hello, World!")
sleep(1)
sense.show_message("Hello, World!", text_colour=(0, 0, 255), back_colour=(255, 0, 0), scroll_speed=(0.5))