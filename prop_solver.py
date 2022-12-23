import math

# CONSTANTS
static_thrust = 2  # newtons of desired static thrust
cruising_speed = 30  # mph desired cruising speed
motor_kv = 2300
input_volts = 4.2*4*.3  # motors are optimally efficient at about 30% of their max rpm, so set it to that if u want peak efficiency
blades = 2  # works for 2,3,4 (just use two blades bruh)
air_density = 1.2471  #  (kg/m^3), 1.2471 is for 10 degrees C (like in the morning when I usually fly)
cf = 1  # some constant relating to the prop, just keep it at 1 ig

# SOLVE
rpm = input_volts*motor_kv
blades_const = [None, None, 1, 1.4, 1.7][blades]  # thrust multiplier for each number of blades

raw_diam = ( static_thrust/(0.00000000000283 * rpm**2 * air_density*23.936/29.92 * cf * blades_const * 0.4536 * 9.81) ) ** .25
raw_pitch = cruising_speed / (rpm * 0.000946961947548)

diam = round(raw_diam)
pitch = round(raw_pitch)

thrust = 0.00000000000283 * (rpm**2) * (diam**4) * (air_density*23.936/29.92) * cf * blades_const * 0.4536 * 9.81
fspeed = rpm*pitch*0.000946961947548

blade_perim_speed = cspeed = diam*2.54/100 * math.pi * rpm/60
kilowatts = rpm**3 * diam**4 * pitch / (10.23**17) * cf * blades_const * 735.5/1000
amperage = kilowatts*1000/input_volts

# OUTPUT
print("INPUTS:")
print("Motor kv (rpm/V):", motor_kv)
print("Input voltage (V):", input_volts)
print("Desired static thrust (newtons):", static_thrust)
print("Desired cruising speed (mph):", cruising_speed)

print("\nOUTPUTS:")
print("Motor rpm:", rpm)
print("Optimal diam (in):", raw_diam, "-->", diam)
print("Optimal pitch:", raw_pitch, "-->", pitch)

print("With rounded diam,pitch values:")
print("\tActual thrust (newtons):", thrust)
print("\tActual cruise speed (mph):", fspeed)
print("\tPropeller blade perimeter speed (m/s):", cspeed)
print("\tPower draw (kW):", kilowatts)
print("\tCurrent draw (Amps):", amperage)

