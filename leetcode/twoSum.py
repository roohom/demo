
def reverse1(x):
    if x >= 0:
        li = str(x)
        dic = {}
        for i in range(len(li)):
            dic[i] = li[i]
        lis = list()
        for j in dic.keys():
            lis.append(dic[j])
        lis.reverse()
        a = ""
        for m in lis:
            a = a+str(m)
        int(a)
        print(a)
    elif x < 0:
        x = abs(x)
        li = str(x)
        dic = {}
        for i in range(len(li)):
            dic[i] = li[i]
        lis = list()
        for j in dic.keys():
            lis.append(dic[j])
        lis.reverse()
        a = ""
        for m in lis:
            a = a + str(m)
        b = -int(a)
        print(b)


x = 120
reverse1(x)

