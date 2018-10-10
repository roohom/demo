#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : practice.py
# Author: roohom
# Date  : 2018/9/28 0028


#递归生成器

def flatten(nested):
    try:
        for sublist in nested:
            for element in  flatten(sublist):
                yield element
    except TypeError:
        yield nested

if __name__ == '__main__':
    s = list(flatten([[[1],2],3,4,[5,[6,7]],8]))
    print(s)
