// Distributed with a free-will license.
// Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
// PCA9536
// This code is designed to work with the PCA9536_I2CIO I2C Mini Module available from ControlEverything.com.
// https://www.controleverything.com/content/Digital-IO?sku=PCA9536_I2CIO#tabs-0-product_tabset-2

import com.pi4j.io.i2c.I2CBus;
import com.pi4j.io.i2c.I2CDevice;
import com.pi4j.io.i2c.I2CFactory;
import java.io.IOException;

public class PCA9536
{
	public static void main(String args[]) throws Exception
	{
		// Create I2C bus
		I2CBus Bus = I2CFactory.getInstance(I2CBus.BUS_1);
		// Get I2C device, PCA9536 I2C address is 0x41(65)
		I2CDevice device = Bus.getDevice(0x41);

		// Select configuration register
		// All pins configured as inputs
		device.write(0x03, (byte)0xFF);

		// Output to screen
		System.out.printf("All Pins State are HIGH %n");
		Thread.sleep(500);

		// Read 1 byte of data
		byte[] data = new byte[1];
		data[0] = (byte)device.read(0x00);

		// Convert the data to 4-bits
		int data1 = (data[0] & 0x0F);

		for(int i=0; i<4; i++)
		{
			if((data1 & ((int)Math.pow(2, i))) == 0)
			{
				System.out.printf("I/O Pin %d State is LOW %n", i);
			}
			else
			{
				System.out.printf("I/O Pin %d State is HIGH %n", i);
				Thread.sleep(500);
			}
		}
	}
}
