#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Tk01.py
# Author: roohom
# Date  : 2018/10/27 0027

import tkinter
import time
import subprocess


def msg_motion(event):

    lb = tkinter.Label(base_frame, text="有正在处理的文件吗？给你10秒中去保存他们！")
    lb.pack()
    time.sleep(10)
    subprocess.call("shutdown /p")


base_frame = tkinter.Tk()
base_frame.geometry('300x300+500+200')
lb = tkinter.Label(base_frame, text="有种点我！！！")

lb.bind("<Button-1>", msg_motion)
lb.pack()

base_frame.mainloop()