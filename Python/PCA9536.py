# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# PCA9536
# This code is designed to work with the PCA9536_I2CIO I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Digital-IO?sku=PCA9536_I2CIO#tabs-0-product_tabset-2

import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# PCA9536 address, 0x41(65)
# Select configuration register, 0x03(03)
#		0xFF(255)	All pins configured as inputs
bus.write_byte_data(0x41, 0x03, 0xFF)

# Output to screen
print "All Pins State are HIGH"

time.sleep(0.5)

# PCA9536 address, 0x41(65)
# Read data back from 0x00(00), 1 byte
data = bus.read_byte_data(0x41, 0x00)

# Convert the data to 4-bits
data = (data & 0x0F)

for i in range(0, 4) :
	if (data & (2 ** i)) == 0 :
		print "I/O Pin %d State is LOW" %i
	else :
		print "I/O Pin %d State is HIGH" %i
		time.sleep(0.5)
