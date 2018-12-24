#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: roohom
# Date  : 2018/10/10 0010


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if (nums[i] == target - nums[j]) and (i != j):
                return [i, j]


print(twoSum([3, 2, 1], 5))



