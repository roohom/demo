#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Tk03.py
# Author: roohom
# Date  : 2018/10/28 0028

import tkinter


def msg():
    name = e1.get()
    pwd = e2.get()

    t1 = len(name)
    t2 = len(pwd)

    if name == "111" and pwd == "222":
        lb3["text"] = "登录成功！"
    else:
        lb3["text"] = "用户名或密码错误"
        e1.delete(0, t1)
        e2.delete(0, t2)


baseFrame = tkinter.Tk()
baseFrame.geometry("300x300+500+200")

lb1 = tkinter.Label(baseFrame, text="用户名")
lb1.grid(row=0, column=0, sticky=tkinter.W)

e1 = tkinter.Entry(baseFrame)
e1.grid(row=0, column=1, sticky=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="密码")
lb2.grid(row=1, column=0, sticky=tkinter.W)

e2 = tkinter.Entry(baseFrame)
e2.grid(row=1, column=1, sticky=tkinter.E)
e2["show"] = "*"

lb3 = tkinter.Label(baseFrame, text="")
lb3.grid(row=3)

btn = tkinter.Button(baseFrame, text="登录", command=msg)
btn.grid(row=2, column=1, sticky=tkinter.E)

baseFrame.mainloop()
