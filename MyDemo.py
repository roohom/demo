#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : MyDemo.py
# Author: roohom
# Date  : 2018/9/17 0017


'''
刷题脚本
    - python对文件读写等操作的强大功能
        - 使用docx模块对docx文档进行读写
            - python不支持直接打开并读取word文档，因此需要使用方法将doc转化为docx,方法详见doc_to_docx.py
    - 原理
        - 打开经转化后的docx文档，并逐行读文件内容
        - 判断是否读到“正确内容”语句
            - 是，设置用户输入，提示输入用户的答案
            - 否，继续读操作
        - 比较用户的答案与正确答案是否一样
            - 是，输出正确提示
            - 否，输出错误提示
        - 继续下一题，重复上述操作
    - 拓展延伸
         - 可以在程序主入口处设置用户输入，输入用户想要打开的路径、文件，程序根据文件名、路径等进行上述操作
         - 可以根据用户输入情况设置加分减分，并根据全部答案情况，分析错误题目，后续将错题重修整理收集，反馈给用户
'''

import docx
'''
字符串比较的一种麻烦方法：

def comparison(a, b):
    ib=0
    for ia in range(len(a)):
        if ord(a[ia:ia+1])-ord(b[ib:ib+1])==0:
            ib=ib+1
            if ib==len(b):
                print('你的答案正确！')
        else:
            print('你的答案错误！')
            break
'''

def comparison(a, b):
    if a == b :
        print("你的答案正确！")
    else:
        print("你的答案错误！")

if __name__ == '__main__':
    file = docx.Document(r"D:\学习区\Python\python二级考试试题\选择题\python二级考试试题01.docx")
    print("==================全国计算机二级考试之Python刷题==================")

    for p in file.paragraphs:
        m = p.text
        if "正确答案： " in m:
            ans = input("请输入你的答案：")
            a = "正确答案： {0} ".format(ans)
            print(a)
            b = m
            print(b)
            comparison(a, b)
            print()
            print("==================全国计算机二级考试之Python刷题==================")
        else:
            print(m)

