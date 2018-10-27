#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Tk02.py
# Author: roohom
# Date  : 2018/10/27 0027

from tkinter import *

def msg(self):
    print("hello stdout...")
    top = Frame()
    top.pack()
    Label(top, text="hello world").pack(side=TOP)
    widget = Button(top, text="press", command=msg)
    widget.pack(side=BOTTOM)
    top.mainloop()

msg(self=1)