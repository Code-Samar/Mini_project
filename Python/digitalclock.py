from tkinter import Tk 
from tkinter import Label
import time

root = Tk()
root.title("clock")


def present_time():
    display_time = time.strftime("%H:%M:%S")
    digit_clock.config(text=display_time)
    digit_clock.after(200,present_time)
    
digit_clock = Label(root, font=("arial",75),bg="white",fg="black")
digit_clock.pack()

present_time()

root.mainloop()