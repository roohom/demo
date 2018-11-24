from urllib import request


if __name__ == '__main__':
    url = "https://study.163.com/"

    rsp = request.urlopen(url)

    html = rsp.read()

    print(html.decode())
    