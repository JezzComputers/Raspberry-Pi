# Replace sence_emu with sence_hat for use with physical HAT

from sense_emu import SenseHat
sense = SenseHat()
sense.clear()

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)