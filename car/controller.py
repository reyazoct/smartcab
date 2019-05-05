from flask import Flask
#from . import *
#from __future__ import *
import RPi.GPIO as gpio

app = Flask(__name__)
in1 = 17
in2 = 22
in3 = 23
in4 = 24

gpio.setmode(gpio.BCM)
gpio.setup(in1,gpio.OUT)
gpio.setup(in2,gpio.OUT)
gpio.setup(in3,gpio.OUT)
gpio.setup(in4,gpio.OUT)

def right():
    gpio.output(in1,False)
    gpio.output(in2,True)
    gpio.output(in3,False)
    gpio.output(in4,True)

def reverse():
    gpio.output(in1,False)
    gpio.output(in2,True)
    gpio.output(in3,True)
    gpio.output(in4,False)

def forward():
    gpio.output(in1,True)
    gpio.output(in2,False)
    gpio.output(in3,False)
    gpio.output(in4,True)

def stop():
    gpio.output(in1,False)
    gpio.output(in2,False)
    gpio.output(in3,False)
    gpio.output(in4,False)

def left():
    gpio.output(in1,True)
    gpio.output(in2,False)
    gpio.output(in3,True)
    gpio.output(in4,False)

@app.route('/forward')
def fwd():
    forward()
    return "Forward"

@app.route('/left')
def left_turn():
    left()
    return "Turn Left"

@app.route('/right')
def right_turn():
    right()
    return "Turn Right"

@app.route('/stop')
def stp():
    stop()
    return "Stop"

@app.route('/reverse')
def rev():
    reverse()
    return "Reverse"

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.100')

