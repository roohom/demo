#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: roohom
# Date  : 2018/10/10 0010

import psutil
import os,datetime


def main():
        print("电脑的开机时间")

        # 调用psutil.boot_time()函数返回开机的时间戳
        dt = datetime.datetime.fromtimestamp(psutil.boot_time())
        # 返回一个datetime对象
        print(dt.strftime("%Y-%m-%d,%H:%M:%S"))


if __name__=="__main__":
    main()

