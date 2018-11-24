from urllib import request


if __name__ == '__main__':
    url = "https://study.163.com/"

    rsp = request.urlopen(url)

    print(type(rsp))
    print(rsp)

    print("URL: {}".format(rsp.geturl()))
    print("Info: {}".format(rsp.info()))
    print("Code: {}".format(rsp.getcode()))


