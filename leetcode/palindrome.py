"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

"""


def isPalindrome(x):
    str_x = str(x)
    l = [i for i in str_x]
    li = []
    if x >= 0:
        for j in range(len(l)):
            li.append(l[-(j+1)])
        if l == li:
            return True
        else:
            return False
    else:
        return False


x = 121
a = isPalindrome(x)
print(a)

