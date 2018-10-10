#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 批量将doc转换为docx.py
# Author: roohom
# Date  : 2018/9/17 0017


'''
使用Word批量将doc转化为docx
    - 调用win32com，打开Word应用程序
    - 打开doc
    - 保存成docx
    - 关闭word
    - 转入下一个doc并重复上述操作

'''

from win32com import client as wc

def doSaveAas():
    word = wc.Dispatch('Word.Application')
    #延时10秒钟，防止由于系统配置原因还没打开Word就进行下一步程序
    #time.sleep(5)
    doc = word.Documents.Open(r'{0}'.format(word_name))  # 目标路径下的文件
    doc.SaveAs(r'{0}'.format(word_docx_name), 16)  # 转化后路径下的文件，16表示docx格式
    doc.Close()
    word.Quit()

if __name__ == '__main__':
    k = 1
    i = 3
    j = 3
    while True:
        word_name = "D:\学习区\Python\python二级考试试题\选择题\python二级考试试题{0}.doc".format(i)
        word_docx_name = "D:\学习区\Python\python二级考试试题\选择题\python二级考试试题{0}".format(j)
        doSaveAas()
        i += 1
        j += 1
        print("已完成{0}个word从doc到docx的转换".format(k))
        k += 1