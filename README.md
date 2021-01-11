# openmv-lapan
This is my internship project in Pustekroket LAPAN. I use OpenMV Cam M7 for this project, and then capture/stream the image data through UART communication protocol.

## How It Works
This works is based on Wil Selby [openMV_cam](https://github.com/wilselby/openmv_cam). I updated this project to Python 3 and changed the communication from USB VCP to UART. For testing, I used my laptop and Arduino UNO as USB-to TTL. Then, I sent the image data to laptop with a Python (ver. 3.8) program and OpenCV library (ver. 4.3.0.38).

Use openmv_main.py as main.py program for OpenMV. For testing in your PC, use camstream.py to stream camera feed or camcapture.py to output image data as JPG file.
