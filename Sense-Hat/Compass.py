# Replace sence_emu with sence_hat for use with physical HAT

from sense_emu import SenseHat
sense = SenseHat()
sense.clear()
        
orientation = sense.get_gyroscope_raw()
north = sense.get_compass()
print(north)