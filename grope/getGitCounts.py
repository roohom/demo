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
import requests

git_name = "roohom"
url = "https://github.com/{}".format(git_name)
rsp = requests.get(url)
rsp.encoding = "utf-8"
l = list(rsp.text)
s = ",".join(l)
print(s)
