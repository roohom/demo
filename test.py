#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: roohom
# Date  : 2018/10/10 0010




def upstairs(step):
    if (step % 2 == 1) & (step % 3 == 2) & (step % 4 == 3) & (step % 5 == 4) & (step % 6 == 5) & (step % 7 == 0):
        print("这个数是：",step)
        return True
    else:
        return False


if __name__ == '__main__':
    step = 0
    while True:
        upstairs(step)
        step += 1
        if upstairs(step):
            print("找到了！")
            break
        else:
            print("执行到我了！")

