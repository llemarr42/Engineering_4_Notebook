import time

# Import the LSM303 module.
import Adafruit_LSM303

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

# Note you can change the I2C address by passing an i2c_address parameter like:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)


# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 20
shape_width = 20
top = (height/2)+10
bottom = (height/2)-10
# Move left to right keeping track of the current x position for drawing shapes.
x = padding

print('Printing accelerometer & magnetometer X, Y, Z axis values, press Ctrl-C to quit...')
while True:
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    print('Accel X={0}, Accel Y={1}, Accel Z={2}, Mag X={3}, Mag Y={4}, Mag Z={5}'.format(
          accel_x, accel_y, accel_z, mag_x, mag_y, mag_z))
    
    draw.line((0, 32, 128, 32), fill=255)

    # Draw an ellipse.
    #draw.ellipse((x, top+(accel_x/15) , x+shape_width, bottom+(accel_x/15)), outline=255, fill=0)
    draw.ellipse((20, 20 , 40, 40), outline=255, fill=0)
    x += shape_width+padding
    
    # Draw an ellipse.
    draw.ellipse((x, top+(accel_y/15) , x+shape_width, bottom+(accel_y/15)), outline=255, fill=0)
    x += shape_width+padding
    
    # Draw an ellipse.
    draw.ellipse((x, top+(accel_z/15) , x+shape_width, bottom+(accel_z/15)), outline=255, fill=0)
    x += shape_width+padding
    
    
    # Display image.
    disp.image(image)
    disp.display()

    # Wait half a second and repeat.
    time.sleep(0.5)
