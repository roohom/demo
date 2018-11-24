from urllib import request,parse

"""
使用parse模块对字符进行编码
"""


if __name__ == '__main__':
    url = "https://www.baidu.com/s?"
    wd = input("Plz input your keyword here:")

    qs ={
        "wd": wd
    }

    rsp = parse.urlencode(qs)
    print(rsp)

    fullurl = url+rsp
    print(fullurl)

    rst = request.urlopen(fullurl)
    html = rst.read().decode()

    print(html)
