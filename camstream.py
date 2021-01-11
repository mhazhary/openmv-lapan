"""Python program for host.
Stream JPEG image from OpenCV Cam M7 camera data.
Transferred to host using UART.
"""
# Python libraries
import sys
import struct
import serial
import serial.tools.list_ports
import cv2
import numpy as np

# Print available port
print("\nAvailable Ports:\n")
for port, desc, hwid in serial.tools.list_ports.comports():
    print("{} : {} [{}]".format(port, desc, hwid))
sys.stdout.write("\nPlease enter a port name: ")
sys.stdout.flush()
port = input()
#port = '/dev/ttyACM1'
print("")
sys.stdout.flush()
# Serial port initialization
sp = serial.Serial(port, baudrate=115200, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_EVEN, xonxoff=False, rtscts=True,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=None, dsrdtr=True)

while True:
    # Read data from the serial buffer
    sp.write(b'snap')
    sp.flush()
    size = struct.unpack('<L', sp.read(4))[0]
    buf = sp.read(size)
    # Use numpy to construct an array from the bytes
    x = np.frombuffer(buf, dtype='uint8')
    # Decode the array into an image
    img = cv2.imdecode(x, cv2.IMREAD_UNCHANGED)
    cv2.imshow("Stream:", img)
    key = cv2.waitKey(20)
    if key == 27:
        #sp.close()
        cv2.destroyWindow("Stream:")
        break
