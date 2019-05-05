import io
import socket
import struct
import time
import picamera
#from __future__ import *

print "about to connect"
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "got socket"
client_socket.connect(('192.168.0.101', 8000))
print "finish connection"
connection = client_socket.makefile('wb')


try:
    with picamera.PiCamera() as camera:
        camera.resolution = (320,240)
        camera.framerate = 10
        time.sleep(2)
        start = time.time()
        stream = io.BytesIO()

        for foo in camera.capture_continuous(stream, 'jpeg', use_video_port = True):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())
            
            if time.time() - start > 90:
                break
            stream.seek(0)
            stream.truncate()
            
    connection.write(struct.pack('<L', 0))
except socket.error, e:
    print e
finally:
    connection.close()
    client_socket.close()
    print 'connection closed'
