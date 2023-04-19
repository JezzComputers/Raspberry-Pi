# Replace sence_emu with sence_hat for use with physical HAT

from sense_emu import SenseHat
sense = SenseHat()
sense.clear()

sense.set_pixel(1, 1, (0, 255, 0))