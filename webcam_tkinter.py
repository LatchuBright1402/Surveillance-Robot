#import the necessary libraries
from future.moves import tkinter
import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
from tkinter import *


#OPEN WEBCAM
cap = cv2.VideoCapture(0)

#SET THE SIZE OF THE VIDEO FRAME
width, height = 600, 600



cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

window_main = tkinter.Tk(className='LiBot Digital Console', )

window_main.geometry("800x800")
window_main.configure()
window_main.bind('<Escape>', lambda e: window_main.quit())
#bg=PhotoImage(file='Lakshmanaprakash.jpg')
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

def Forward():
   print('LiBot Moving Forward')


def Backward():
   print('LiBot Moving Backward')


def Left():
   print('LiBot Moving Left')


def Right():
   print('LiBot Moving Right')


def Stop():
   print('LiBot Stopped')

button_forward = tkinter.Button(window_main, text="FORWARD", activeforeground="green", activebackground="red",relief=SUNKEN ,command=Forward)
button_forward.config(bg="red",width=20, height=2)
#button_forward.place(x = 400, y = 400)
button_backward = tkinter.Button(window_main, text="BACKWARD",activeforeground="green", activebackground="red" , command=Backward)
button_backward.config(width=20, height=2)

button_left = tkinter.Button(window_main, text="LEFT",activeforeground="green", activebackground="red" , command=Left)
button_left.config(width=20, height=2)

button_right = tkinter.Button(window_main, text="RIGHT",activeforeground="green", activebackground="red" , command=Right)
button_right.config(width=20, height=2)

button_stop = tkinter.Button(window_main, text="STOP",activeforeground="green", activebackground="red" , command=Stop)
button_stop.config(width=20, height=2)

button_exit = tkinter.Button(window_main, text ="EXIT",activeforeground="green", activebackground="red" , command= window_main.destroy)


#button_submit.pack()
button_forward.pack()
button_backward.pack()
button_left.pack()
button_right.pack()
button_stop.pack()
button_exit.pack()

show_frame()
window_main.mainloop()