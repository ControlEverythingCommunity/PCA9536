# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# PCA9536
# This code is designed to work with the PCA9536_I2CIO I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Digital-IO?sku=PCA9536_I2CIO#tabs-0-product_tabset-2

from OmegaExpansion import onionI2C
import time

# Get I2C bus
i2c = onionI2C.OnionI2C()

# PCA9536 address, 0x41(65)
# Select configuration register, 0x03(03)
#		0xFF(255)	All pins configured as inputs
i2c.writeByte(0x41, 0x03, 0xFF)

# Output to screen
print "All Pins State are HIGH"

time.sleep(0.5)

# PCA9536 address, 0x41(65)
# Read data back from 0x00(00), 1 byte
data = i2c.readBytes(0x41, 0x00, 1)

# Convert the data to 4-bits
data[0] = (data[0] & 0x0F)

for i in range(0, 4) :
	if (data[0] & (2 ** i)) == 0 :
		print "I/O Pin %d State is LOW" %i
	else :
		print "I/O Pin %d State is HIGH" %i
		time.sleep(0.5)
