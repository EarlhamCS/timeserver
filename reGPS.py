import serial
import re
#Goals:
#make a timer, write to /dev/null.
#try to get .1 or .01 second resolution.
#   the NMEA output itself comes with a millisecond resolution.
#As long as the baud rate is correct, setting the number of 
#data bits produces incomplete but extant output.
#'screen /dev/ttyUSB0 4800,cs{6,8}' both produce one sentence per line.
#				    but cs6 has certain fields missing.
#'screen /dev/ttyUSB0 4800,cs7'     does not produce one sentence per line.
ser = serial.Serial(
port="/dev/ttyUSB0",
baudrate=4800, 
parity=serial.PARITY_NONE,
bytesize=serial.EIGHTBITS,
stopbits=serial.STOPBITS_ONE,
timeout=None)

sampleSize = 300
sentenceID = "\$GPRMC"
ser.open()
while True:
    grab = ser.read(sampleSize)
    csv = grab.split(',')
    for i in range(len(csv)):
        if re.search(sentenceID, csv[i]):
            print csv[i + 1]
ser.close()
