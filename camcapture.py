"""Python program for host.
Capture JPEG image from OpenCV Cam M7 camera data, one at a time.
Transferred to host using UART.
"""
import sys
import struct
import serial
import serial.tools.list_ports
print("\nAvailable Ports:\n")
for PORT, DESC, HWID in serial.tools.list_ports.comports():
    print("{} : {} [{}]".format(PORT, DESC, HWID))
sys.stdout.write("\nPlease enter a PORT name: ")
sys.stdout.flush()
PORT=input()
print("")
sys.stdout.flush()
sp = serial.Serial(PORT, baudrate=115200, bytesize=serial.EIGHTBITS,
                    parity=serial.PARITY_EVEN, xonxoff=False, rtscts=True,
                    stopbits=serial.STOPBITS_ONE,
                    timeout=None, dsrdtr=True)
sp.write(b'snap')
sp.flush()
size = struct.unpack('<L', sp.read(4))[0]
img = sp.read(size)
sp.close()

with open("img.jpg", "wb") as f:
    f.write(img)
