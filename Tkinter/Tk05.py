#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Tk05.py
# Author: roohom
# Date  : 2018/10/28 0028

# 级联菜单

import tkinter

baseFrame = tkinter.Tk()
baseFrame.title("demo")
baseFrame.geometry("300x450+500+150")                # 设置窗口大小及位置，300x450，位置是x：500， y：150

menuBar = tkinter.Menu(baseFrame)
tmenuBar = tkinter.Menu(baseFrame)
for item in ["文件", "编辑", "查看", "工具", "关于"]:
    tmenuBar.add_command(label=item)

menuBar.add_cascade(label="刷新")
menuBar.add_cascade(label="跳转", menu=tmenuBar)

baseFrame["menu"] = menuBar


baseFrame.mainloop()
