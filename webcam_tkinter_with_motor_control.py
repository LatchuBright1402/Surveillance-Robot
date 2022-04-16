#import the necessary libraries
from future.moves import tkinter
import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
from tkinter import *

import RPi.GPIO as IO
IO.setwarnings(False)
IO.setmode(IO.BCM) #or IO.BOARD
from time import sleep
import sys, tty, termios, time
#import the necessary libraries
from future.moves import tkinter
import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
from tkinter import *


m11 = 6#31
m12 = 13#33
m21 = 19#35
m22 = 26#36
IO.setup(m11, IO.OUT)
IO.setup(m12, IO.OUT)
IO.setup(m21, IO.OUT)
IO.setup(m22, IO.OUT)


def Stop():  # Perfect

    IO.output(m11, 0)
    IO.output(m12, 0)
    IO.output(m21, 0)
    IO.output(m22, 0)
    print("stop")


def Forward():  # Perfect

    IO.output(m11, 1)
    IO.output(m12, 0)
    IO.output(m21, 0)
    IO.output(m22, 1)
    print("Forward")


def Backward():  # Perfect

    IO.output(m11, 0)
    IO.output(m12, 1)
    IO.output(m21, 1)
    IO.output(m22, 0)
    print("Backward")


def Left():
    IO.output(m11, 0)
    IO.output(m12, 1)
    IO.output(m21, 0)
    IO.output(m22, 1)
    print("Left")


def Right():
    IO.output(m11, 1)
    IO.output(m12, 0)
    IO.output(m21, 1)
    IO.output(m22, 0)
    print("Right")

#OPEN WEBCAM
cap = cv2.VideoCapture(0)

#SET THE SIZE OF THE VIDEO FRAME
width, height = 600, 600

cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

window_main = tkinter.Tk(className='LiBot Digital Console', )
window_main.geometry("800x800")
window_main.bind('<Escape>', lambda e: window_main.quit())
lmain = Label(window_main)
lmain.pack()

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
'''
def Forward():
   print('LiBot Moving Forward')


def Backward():
   print('LiBot Moving Backward')


def Left():
   print('LiBot Moving Left')


def Right():
   print('LiBot Moving Right')


def Stop():
   print('LiBot Stopped')'''

button_forward = tkinter.Button(window_main, text="Forward", command=Forward)
button_forward.config(width=20, height=2)
button_backward = tkinter.Button(window_main, text="Backward", command=Backward)
button_backward.config(width=20, height=2)
button_left = tkinter.Button(window_main, text="Left", command=Left)
button_left.config(width=20, height=2)
button_right = tkinter.Button(window_main, text="Right", command=Right)
button_right.config(width=20, height=2)
button_stop = tkinter.Button(window_main, text="Stop", command=Stop)
button_stop.config(width=20, height=2)


#button_submit.pack()
button_forward.pack()
button_backward.pack()
button_left.pack()
button_right.pack()
button_stop.pack()

show_frame()
window_main.mainloop()