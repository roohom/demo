
# coding:utf-8
# 运行当前脚本来获取当前电脑及python的配置信息。
import sys, platform
# 先看python。
a = sys.version_info
print("当前python版本号是{a[0]}.{a[1]}.{a[2]}".format(a=a))

ret = {}
# 当前操作系统
plat_form = platform.platform()
if "Linux" in plat_form:
    ret["plat_form"] = "Linux"
elif "Windows" in plat_form:
    ret["plat_form"] = "Windows"
else:
    ret['plat_form'] = "Mac"

ret["version"] = platform.version()
ret['version_bit'] = platform.architecture()[0][0:2]
print("当前系统是{ret[plat_form]}".format(ret=ret))
print("操作系统版本号是{ret}".format(ret=ret['version'].split(" ")[0]))
print("{ret[version_bit]}操作系统".format(ret=ret))
