# Replace sence_emu with sence_hat for use with physical HAT

from sense_emu import SenseHat
sense = SenseHat()
sense.clear()

acceleration = sense.get_accelerometer_raw()

x = acceleration["x"]
y = acceleration["y"]
z = acceleration["z"]

x = round(x)
y = round(y)
z = round(z)

print("x =", x, "y =", y, "z =", z)