# Replace sence_emu with sence_hat for use with physical HAT

from sense_emu import SenseHat
sense = SenseHat()
sense.clear()

orientation = sense.get_orientation()

pitch = orientation["pitch"]
roll = orientation["roll"]
yaw = orientation["yaw"]

print("pitch=", pitch, " roll=", roll, " yaw=", yaw)