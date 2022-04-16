import RPi.GPIO as IO
IO.setwarnings(False)
IO.setmode(IO.BCM) #or IO.BOARD
import sys, tty, termios, time
from time import sleep

m11 = 6#31
m12 = 13#33
m21 = 19#35
m22 = 26#36

IO.setup(m11,IO.OUT)
IO.setup(m12,IO.OUT)
IO.setup(m21,IO.OUT)
IO.setup(m22,IO.OUT)

def stop(): #Perfect
    
    IO.output(m11,0)
    IO.output(m12,0)
    IO.output(m21,0)
    IO.output(m22,0)
    print("stop")
    
def forward():#Perfect

    IO.output(m11,1)
    IO.output(m12,0)
    IO.output(m21,0)
    IO.output(m22,1)
    print("Forward")

def backward(): #Perfect

    IO.output(m11,0)
    IO.output(m12,1)
    IO.output(m21,1)
    IO.output(m22,0)
    print("Backward")

def left():

    IO.output(m11,0)
    IO.output(m12,1)
    IO.output(m21,0)
    IO.output(m22,1)
    print("Left")

def right():

    IO.output(m11,1)
    IO.output(m12,0)
    IO.output(m21,1)
    IO.output(m22,0)
    print("Right")

while True:
    key = ord(sys.stdin.read(1))
    if (key==119):
        print("w")
        forward()

    elif (key==115):
        print("S")
        backward()

    elif (key==97):
        print("a")
        left()

    elif (key==100):
        print("d")
        right()

    elif (key==120):
        print("x")
        stop()
#key==119 - "w"
#key==97 - "a"
#key==115 - "s"
#key==100 - "d"
#key==120 - "x"
        
