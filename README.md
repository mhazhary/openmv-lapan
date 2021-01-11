# openmv-lapan
This is my internship project in Pustekroket LAPAN. I use OpenMV Cam M7 for this project, and then capture/stream the image data through UART communication protocol.

## How It Works
This works is based on Wil Selby [openMV_cam](https://github.com/wilselby/openmv_cam). I updated this project to Python 3 and changed the communication from USB VCP to UART. For testing, I used my laptop and Arduino UNO as USB-to TTL. Then, I sent the image data to laptop with a Python program and OpenCV library.
