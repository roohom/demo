import itchat
import os
import time
import cv2
from PIL import ImageGrab

sendMsg = u"{消息助手}：主人暂时不在，请在哔声后留言：\n哔~"
usageMsg = u"使用方法：\n1.运行CMD命令：cmd xxx (xxx为命令)\n" \
           u"-例如关机命令:\ncmd shutdown -s -t 0 \n" \
           u"2.获取当前电脑用户：cap\n3.启用消息助手(默认关闭)：ast\n" \
           u"4.关闭消息助手：astc\n"\
           u"5.获取屏幕截图：cut"


flag = 0  # 消息助手开关
nowTime = time.localtime()
filename = str(nowTime.tm_mday) + str(nowTime.tm_hour) + str(
    nowTime.tm_min) + str(nowTime.tm_sec) + ".txt"
myfile = open(filename, 'w')
path = r"D:\myFunc\temp\tmp.jpg"


@itchat.msg_register('Text')
def text_reply(msg):
    global flag

    message = msg['Text']
    fromName = msg['FromUserName']
    toName = msg['ToUserName']

    if toName == "filehelper":
        if message == "cap":
            cap = cv2.VideoCapture(0)
            ret, img = cap.read()
            cv2.imwrite("weixinTemp.jpg", img)
            itchat.send('@img@%s' % u'weixinTemp.jpg', 'filehelper')
            cap.release()
            print("用户照片发送成功！")
        if message[0:3] == "cmd":                              # 执行cmd命令
            os.system(message.strip(message[0:4]))
        if message == "ast":                                   # 打开消息助手
            flag = 1
            itchat.send("消息助手已开启", "filehelper")
        if message == "astc":                                  # 关闭消息助手
            flag = 0
            itchat.send("消息助手已关闭", "filehelper")
        if message == "cut":                                   # 获取屏幕截图
            im = ImageGrab.grab()  # 实现截屏功能
            im.save(path, 'JPEG')  # 设置保存路径和图片格式
            itchat.send_image(path, 'filehelper')
    elif flag == 1:
        itchat.send(sendMsg, fromName)
        myfile.write(message)
        myfile.write("\n")
        myfile.flush()


if __name__ == '__main__':
    itchat.auto_login()
    itchat.send(usageMsg, "filehelper")
    itchat.run()
