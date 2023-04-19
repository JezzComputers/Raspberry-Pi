# Replace sence_emu with sence_hat for use with physical HAT

from sense_emu import SenseHat
from time import sleep
sense = SenseHat()
sense.clear()

sense.clear(255, 255, 255)
sleep(1)
sense.clear()