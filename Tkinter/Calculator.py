#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Calculator.py
# Author: roohom
# Date  : 2018/10/28 0028

from tkinter import *


# 画出大致面板


baseFrame = Tk()
baseFrame.title("计算器")
baseFrame.geometry("300x450+500+150")
# 定义面板
# bg代表背景颜色（background）， #dddddd是十六进制表示颜色的一个串
frame_show = Frame(width=300, height=150, bg='#dddddd')
frame_show.pack()

# 定义顶部区域
sv = StringVar()
sv.set('0')

# anchor:定义控件的锚点，e代表右边
# font代表字体
show_label = Label(frame_show, textvariable=sv, \
                  bg='green', width=12, height=1,\
                  font=("黑体", 20, 'bold'),\
                  justify=LEFT, anchor='e')
show_label.pack(padx=10, pady=10)

# 功能函数
def clear():
    print("清零了！")
def fan():
    print("找我啥事啊")


# 功能区域
frame_bord = Frame(width=400, height=350, bg="#cccccc")

b_AC = Button(frame_bord, text="AC", width=6, height=1, command=clear).grid(row=0, column=0)

button_clear = Button(frame_bord, text='±',width=6, height=1,\
                      command=clear).grid(row=0, column=1)
button_fan = Button(frame_bord, text='%', width=6, height=1,\
                    command=fan).grid(row=0, column=2)
button_ce = Button(frame_bord, text='/', width=6, height=1,\
                   command=clear).grid(row=0, column=3)

frame_bord.pack(padx=10, pady=10)
baseFrame.mainloop()