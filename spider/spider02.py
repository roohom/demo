from urllib import request
import chardet

if __name__ == '__main__':
    url = "https://study.163.com/"

    rsp = request.urlopen(url)
    html = rsp.read()

    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    html = html.decode(cs.get("encoding","utf-8"))

    print(html)

