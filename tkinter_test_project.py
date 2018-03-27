# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:23:20 2018

@author: Shenghai
"""

from tkinter import Tk, Label, Button, Checkbutton
from tkinter import *
import datetime
# Here, we are creating our class, Window, and inheriting from the Frame class. 
# Frame is a class from the tkinter module. (see Lib/tkinter/__init__)

# Then we define the settings upon initialization. This is the master widget.
#class Window(Frame):
#    
#    def __init__(self, master=None):
#        Frame.__init__(self, master)
#        self.master = master
        
today = datetime.date.today()

def clicked():
    dwnld.configure(text = "Statements are on their way")

window = Tk()

window.title("Wells Fargo Scraper")

window.geometry('1000x800')

lbl = Label(window, text = str(today), font=('Arial', 16))

lbl.grid(column=0, row = 0)

dwnld = Button(window, text="Download", font=('Arial', 10), command = clicked)

dwnld.grid(column = 100, row = 100)

chk = Checkbutton(window, text='Choose')

window.mainloop()