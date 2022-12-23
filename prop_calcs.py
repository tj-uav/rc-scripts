import math


diam = 7
pitch = 4
cf = 1
rpm = 8000
density = 1.2471
blades = 2  # NOTE: must be 2, 3, or 4 only

thrust = None  # thrust generated in newtons
cspeed = None  # blade perimeter speed in m/s
fspeed = None  # estimated flying speed in mph
kilowatts = None  # motor power draw

blades_const = [None, None, 1, 1.4, 1.7][blades]  # thrust multiplier for each number of blades
thrust = 0.00000000000283 * (rpm**2) * (diam**4) * (density*23.936/29.92) * cf * blades_const * 0.4536 * 9.81
cspeed = diam*2.54/100 * math.pi * rpm/60
kilowatts = rpm**3 * diam**4 * pitch / (10.23**17) * cf * blades_const * 735.5/1000
fspeed = rpm*pitch*0.000946961947548

print("Static thrust (newtons):", thrust)
print("Flight speed (mph):", fspeed)
print("Propeller blade perimeter speed (m/s):", cspeed)
print("Power draw (kW):", kilowatts)
