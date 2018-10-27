#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Tkinter.py
# Author: roohom
# Date  : 2018/10/27 0027

import tkinter

base = tkinter.Tk()                                # 创建总面板

base.wm_title("Hello Tkinter!")
lb1 = tkinter.Label(base, text="Python Label")    # 父组件是base， 属性设置为text="Python Label"
lb1.pack()
lb2 = tkinter.Label(base, text="Black", background="black")
lb2.pack()
lb3 = tkinter.Label(base, text="Green", background="green")
lb3.pack()

tkinter.mainloop()                                 # 启动总面板的消息循环
