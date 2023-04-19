# Replace sence_emu with sence_hat for use with physical HAT

from sense_emu import SenseHat
sense = SenseHat()
sense.clear()

pres = sense.get_pressure()
humi = sense.get_humidity()
temp = sense.get_temperature()
ptemp = sense.get_temperature_from_pressure()

avg_temp = (temp + ptemp) / 2

print("pres = ", pres, "humi = ", humi, "temp = ", temp, "ptemp = ". ptemp, "avg_temp = ", avg_temp)