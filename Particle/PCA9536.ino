// Distributed with a free-will license.
// Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
// PCA9536
// This code is designed to work with the PCA9536_I2CIO I2C Mini Module available from ControlEverything.com.
// https://www.controleverything.com/content/Digital-IO?sku=PCA9536_I2CIO#tabs-0-product_tabset-2

#include <application.h>
#include <spark_wiring_i2c.h>
#include <math.h>

// PCA9536 I2C address is 0x41(65)
#define Addr 0x41

int data = 0;
void setup()
{
  // Set variable
  Particle.variable("i2cdevice", "PCA9536");
  
  // Initialise I2C communication as Master
  Wire.begin();
  // Initialise serial communication, set baud rate = 9600
  Serial.begin(9600);

  // Start I2C transmission
  Wire.beginTransmission(Addr);
  // Select configuration register
  Wire.write(0x03);
  // Select GPIO as input
  Wire.write(0xFF);
  // Stop I2C transmission
  Wire.endTransmission();

  // Output to dashboard
  Particle.publish("All Pins State are ","HIGH");
  delay(1000);
}

void loop()
{
  unsigned int data;
  
  // Start I2C transmission
  Wire.beginTransmission(Addr);
  // Select input port register
  Wire.write(0x00);
  // Stop I2C transmission
  Wire.endTransmission();
    
  // Request 1 byte of data
  Wire.requestFrom(Addr, 1);
  
  // Read 1 byte of data 
  if(Wire.available() == 1)
  {
    data = Wire.read();
  }

  // Convert the data to 4-bits
  data = data & 0x0F;
  
  for(int i = 0; i < 4;  i++)
  {
    if((data & ((unsigned int)pow(2, i))) == 0)
    {
      Particle.publish("I/O Pin ", String(i) + " State is LOW");
    }
    else
    {
      Particle.publish("I/O Pin ", String(i) + " State is HIGH");
    }
    delay(1000);
  }
}

