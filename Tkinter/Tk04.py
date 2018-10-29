#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Tk04.py
# Author: roohom
# Date  : 2018/10/28 0028

import tkinter
baseFrame = tkinter.Tk()
baseFrame.title("demo")
baseFrame.geometry("300x450+500+150")                # 设置窗口大小及位置，300x450，位置是x：500， y：150

menuBar = tkinter.Menu(baseFrame)

for item in ["文件", "编辑", "查看", "工具", "关于"]:
    menuBar.add_command(label=item)

baseFrame["menu"] = menuBar


baseFrame.mainloop()
