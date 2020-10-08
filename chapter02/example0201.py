#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Project Name: python4desktop - Created Date: Thursday September 17th 2020
# Author: loitd - Email: loitranduc@gmail.com
# Description: example0201.py
# Copyright (c) 2020 loitd. WWW: https://github.com/loitd
# -----
# Last Modified: Thursday September 17th 2020 9:29:07 am By: loitd
# -----
# HISTORY:
# Date      	By    	Comments
# ----------	------	----------------------------------------------------------
# 2020-09-17	loitd	Initialized
###

from tkinter import *

def hello():
    print("Hello")

def makeform(root, fields):
    '''Making the form based on the root'''
    for field in fields:
        # Frame = a container widget to organize other widgets.
        row = Frame(root)
        lbl = Label(row, width=16, text=field, anchor="w")
        # Entry = single-line text field.
        ent = Entry(row, width=58)
        # pack = organizes widgets in blocks before placing them in the parent widget.
        # expand = true => fill space of parent
        # fill = NONE | X (horizontally) | Y (vertically) | BOTH
        # side = TOP | BOTTOM | LEFT | RIGHT
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lbl.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        # Insert a sample text
        ent.insert(0, "https://github.com/loitd/python4desktop")
    # Create a frame to store all buttons
    btnFrame = Frame(root)
    btnFrame.pack(side=BOTTOM, expand=YES, fill=X)
    # Create a button with foreground text color
    btn1 = Button(btnFrame, text="Do it", width=10, fg="blue", command=hello)
    btn1.pack(side=RIGHT, padx=5, pady=5)
    # Create a normal button
    btn2 = Button(btnFrame, text="Reset", command=None)
    btn2.pack(side=RIGHT, padx=5, pady=5)
    # Create a button with image and text on it
    imgexit = PhotoImage(file=r"imgexit.gif").subsample(6,7)
    btn3 = Button(btnFrame, text="Exit", image=imgexit, compound=LEFT, width=60, command=root.quit)
    btn3.image = imgexit # is a must to keep a reference
    btn3.pack(side=LEFT, padx=5, pady=5)

if __name__ == "__main__":
    root = Tk()
    root.iconbitmap("py4de.ico")
    root.title("Python4Desktop")
    fields = ["Label 1", "Label 2", "Label 3"]
    makeform(root, fields)
    root.mainloop()