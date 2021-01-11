import sensor, image, time, ustruct, pyb
uart = pyb.UART(3, 115200, timeout_char=1000)
uart.init(115200, bits=8, parity=0, stop=1, timeout_char=1000)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.VGA)
sensor.skip_frames(time = 2000)
while(True):
	pyb.LED(2).on()
	cmd = uart.read(4)
	if (cmd == b'snap'):
		pyb.LED(2).off()
		img = sensor.snapshot().compressed()
		uart.write(ustruct.pack("<L", img.size()))
		uart.write(img)
		
