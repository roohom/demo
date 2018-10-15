#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : practice.py
# Author: roohom
# Date  : 2018/9/28 0028

# 找出所有的水仙花数 例如:153 = 1^3+3^3+5^3


# 字符串追加


def str_plus(list):
    l = [str(i) for i in list]
    string = "".join(l)
    return string


def find_daffodil(list):
    while True:
        str_plus(list)
        return str_plus(list)


# 将一个数拆分成各个位数数字并取其三次方之和
def pos_sum(s):
    m = 0
    n = 0
    sum = 0

    for z in range(len(s)):
        x = int(z)
        sum = sum + int(s[x])**3
    return sum


if __name__ == '__main__':
    i = 0
    y = input("请输入你想查找水仙花数的范围：")
    p = int(y)
    for j in range(p):
        list = [i]
        s = find_daffodil(list)
        if pos_sum(s) == i :
            print("找到啦！这是一个水仙花数：",i)
        i += 1
