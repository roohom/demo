#!/usr/bin/env python 
# -*- encoding: utf-8 -*-
# @author: roohom
# @contact: roohom@qq.com
# @site: https://blog.csdn.net/qq_39161804
# @software: PyCharm
# @file: getGitCounts.py
# @time: 2019/1/15 23:58
# @Software:Pycharm

# 获取GitHub上自己contributions数量

import urllib
import urllib3


git_name = input("ENTER YOUR GIT NAME:")
url = "https://github.com/{}".format(git_name)

