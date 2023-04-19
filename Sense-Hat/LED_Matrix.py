# Replace sence_emu with sence_hat for use with physical HAT

from sense_emu import SenseHat
sense = SenseHat()
sense.clear()

r = (255, 0, 0)
g = (0, 255, 0)

pic = [
    r, r, r, r, r, r, r, r,
    g, g, g, g, g, g, g, g,
    r, r, r, r, r, r, r, r,
    g, g, g, g, g, g, g, g,
    r, r, r, r, r, r, r, r,
    g, g, g, g, g, g, g, g,
    r, r, r, r, r, r, r, r,
    g, g, g, g, g, g, g, g
]

sense.set_pixels(pic)