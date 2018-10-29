#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : Tk06.py
# Author: roohom
# Date  : 2018/10/29 0029


"""
本程序功能：
    - 用于对文件的批量整理
    - 对有关键词的文件从一个文件夹移动到另一个指定的文件夹
"""
'''
文档整理脚本
  - 获取批量文档所在的文件夹的地址
        - 手动查阅
        -是全部文档的主目录，主路径path
  - 对每一个文件名进行检索并分类
        - 具有相同关键字的一批文件
  - 对有关键字文件名进行获取地址
        - "path{0}".format(filename)
        - join(path,filename)
  - 判断文件名中是否是自己需要处理的文件名，是的话进行移动操作，即整理
        - 使用if语句进行判断
        - 文件的删除、移动、复制、获取路径使用Python的os和shutil模块
'''
import os
import shutil
import os.path as op
import tkinter

# 获取批量文件处理的总路径


def file_process():
    main_path = e1.get()
    os.chdir("{0}".format(str(main_path)))           # 将解释器的工作路径切换到要处理的文件夹的路径
    names = os.listdir("{0}".format(main_path))      # 获取当前目录下所有要批量处理的文件名names
    myIn = e2.get()
    myDst = e3.get()

    for name in names:                                # 遍历所有的文件名
        if "{0}".format(myIn) in name:
            myScr = op.join(main_path, name)          # 将上一级路径与文件名组合，得到文件的绝对路径，os.path.join(path,path)
            shutil.move(myScr, myDst)                  # 进行文件移动 原来的路径--> 目标路径


baseFrame = tkinter.Tk()
baseFrame.title("文件整理")
baseFrame.geometry("750x300+300+150")

lb1 = tkinter.Label(baseFrame, text="请手动查阅文件夹的路径：", )
lb1.grid(row=0, column=0, sticky=tkinter.W)
e1 = tkinter.Entry(baseFrame)
e1.grid(row=0, column=2, sticky=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="你所要进行归类的关键字：").grid(row=1, column=0, sticky=tkinter.W)
e2 = tkinter.Entry(baseFrame)
e2.grid(row=1, column=2, sticky=tkinter.E)

lb3 = tkinter.Label(baseFrame, text="请输入你所要放置的目标文件夹路径：")
lb3.grid(row=2, column=0, sticky=tkinter.W)
e3 = tkinter.Entry(baseFrame)
e3.grid(row=2, column=2, sticky=tkinter.E)

btn = tkinter.Button(baseFrame, text="开始整理", command=file_process).grid(row=3, column=1)
lb4 = tkinter.Label(baseFrame, text="本程序用于文件的批量整理").grid(row=6, column=1)
lb5 = tkinter.Label(baseFrame, text="输入要整理的文件所在的文件夹，关键字为文件名所包含").grid(row=7, column=1)
lb6 = tkinter.Label(baseFrame, text="输入目标文件夹，程序根据关键字匹配文件，并将其移入目标文件夹").grid(row=8, column=1)
baseFrame.mainloop()
