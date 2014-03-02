__author__ = 'Don Reilly'
import socket
import time
import picamera

client_socket = socket.socket()
client_socket.connect(('54.186.4.203', 8456))

connection = client_socket.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.start_preview()
        time.sleep(2)
        camera.start_recording(connection, format='h264')
        camera.wait_recording(60)
        camera.stop_recording()
finally:
    connection.close()
    client_socket.close()