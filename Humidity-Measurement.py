import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import RPi.GPIO as gpo
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
out = 26
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)
gpo.setup(out,gpo.OUT)
gpo.output(out,gpo.LOW)
    
try:
    # Hardware SPI configuration:
    #SPI_PORT   = 0
    #SPI_DEVICE = 0
    #mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
    
    
    print('Reading MCP3008 values, press Ctrl-C to quit...')
    # Print nice channel column headers.
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
    print('-' * 57)
    # Main program loop.
    while True:
        # Read all the ADC channel values in a list.
        gpo.output(out,gpo.LOW)
        values = [0]*8
        for i in range(8):
            # The read_adc function will get the value of the specified channel (0-7).
            values[i] = mcp.read_adc(i)
        # Print the ADC values.
        print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
        # Pause for half a second.
        gpo.output(out,gpo.HIGH)
        time.sleep(0.5)
        gpo.output(out,gpo.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
        gpo.output(out,gpo.LOW)
        quit()