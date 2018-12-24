__author__ = 'roohom'
# -*-coding:utf-8-*-

from selenium import webdriver
import requests
import urllib
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标操作
from selenium.webdriver.common.keys import Keys  # 导入键值操作
import time


sign_page = "https://hfuucxcy.xuetangx.com/manager#/studentcourselist"  # 登录课程页面

browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
browser.get(sign_page)

myusername = "1605011025"
mypassword = "roohom123"


loginname = browser.find_element_by_xpath("//input[@id='stu-code']")  # 找到账号输入框
password = browser.find_element_by_xpath('//input[@type="password"]')  # 找到密码输入框
# MyID = browser.find_element_by_id("student")  # 找到登录者身份
time.sleep(8)

#submit = browser.find_element_by_id('//input[@name="button"]')  # 找到登录框
loginname.send_keys(myusername)  # 输入账号
password.send_keys(mypassword)  # 输入密码
#submit.click()


# 点击进入课程
# One_step = browser.find_element_by_css_selector('')
# One_step.click()

print("点击就“进入课程”成功了！")
time.sleep(10)

# 各视频的连接：
# 视频3.3


while True:
    time.sleep(3)
    list = [
    "body > div:nth-child(1) > div > div.main > div > section.content-wrapper.fr > div > div > div > ul > li:nth-child(4) > div:nth-child(2) > div > ul > li:nth-child(1) > div > ul",
    'body > div:nth-child(1) > div > div.main > div > section.content-wrapper.fr.fixed-top > div > div > div > ul > li:nth-child(4) > div:nth-child(2) > div > ul > li:nth-child(2) > div > ul',
    'body > div:nth-child(1) > div > div.main > div > section.content-wrapper.fr.fixed-top > div > div > div > ul > li:nth-child(4) > div:nth-child(2) > div > ul > li:nth-child(3) > div > ul',
    '#video-wrap > div.video-main > div.course-structure-tree__wrap > div > ul > li:nth-child(4) > div > div.tree-section-item__wrap > ul > li:nth-child(3) > div > ul',
    '#video-wrap > div.video-header > span.select-chapter',
    '#video-wrap > div.video-main > div.course-structure-tree__wrap > div > ul > li:nth-child(4) > div > div.tree-section-item__wrap > ul > li:nth-child(3) > div > ul > li',
    '#video-wrap > div.video-main > div.course-structure-tree__wrap > div > ul > li:nth-child(4) > div > div.tree-section-item__wrap > ul > li:nth-child(3) > div > ul > li > div > div',
    '//*[@id="video-wrap"]/div[2]/div[2]/div/ul/li[4]/div/div[2]/ul/li[3]/div/div',
    '//*[@id="video-wrap"]/div[2]/div[2]/div/ul/li[4]/div/div[2]/ul/li[3]/div/ul/li/div/div',
    '//*[@id="video-wrap"]/div[2]/div[2]/div/ul/li[4]/div/div[2]/ul/li[3]/div/ul/li/div/div',
    '//*[@id="video-wrap"]/div[2]/div[2]/div/ul/li[4]/div/div[2]/ul/li[2]/div/ul/li/div/div',
    '//*[@id="video-wrap"]/div[2]/div[2]/div/ul/li[4]/div/div[2]/ul/li[3]/div/ul/li/div/div',
    '//*[@id="video-wrap"]/div[2]/div[2]/div/ul/li[4]/div/div[2]/ul/li[3]/div/ul/li',
    '//*[@id="video-wrap"]/div[2]/div[2]/div/ul/li[4]/div/div[2]/ul/li[3]/div/ul',
    '//*[@id="video-wrap"]/div[2]/div[2]/div/ul/li[4]/div/div[2]/ul/li[3]/div/ul/li/div',
    '//*[@id="video-wrap"]/div[2]/div[2]/div/ul/li[4]/div/div[2]/ul/li[3]/div/ul/li/div/div/span',
    '#video-wrap > div.video-main > div.course-structure-tree__wrap > div > ul > li:nth-child(4) > div > div.tree-section-item__wrap > ul > li:nth-child(3) > div > ul > li']

    # 点击视频按钮 视频
    try:
        Auto_cli = browser.find_element_by_css_selector(list[1])
        Auto_cli.click()
    except:
        pass
    print("等待5秒进入点击播放视频...")
    time.sleep(3)

    # 点击播放视频

    mov_click = browser.find_element_by_xpath('//*[@id="video-box"]/div/div/div[1]').click()
    print("等待5秒进入新课程...")
    time.sleep(3)

    print("等待30秒进入点击选择章节...")
    time.sleep(15)  # 等待十二分钟
    print("进入新课播放......")

    # 点击选择章节按钮
    print("等待5秒进入点击选择章节按钮...")
    time.sleep(2)
    two_step = browser.find_element_by_css_selector(list[4]).click()
    print("等待5秒进入点击下一视频...")
    time.sleep(2)
    # 点击下一视频播放按钮
    three_step = browser.find_element_by_xpath(list[7]).click()
    print("......")
    time.sleep(2)

    # 点击新视频
    four_step = browser.find_element_by_css_selector(list[-1])
    time.sleep(2)
    print('等待两秒进入新视频的播放')

    open_click = browser.find_element_by_xpath('//*[@id="video-box"]/div/div/div[1]/div[1]')

    time.sleep(20)
    '''
    browser.implicitly_wait(5)
    internManage = browser.find_element_by_css_selector('#menu-article > dt').click()
    time.sleep(3)
    weekDiary = browser.find_element_by_css_selector('#menu-article > dd > ul > li:nth-child(4) > a').click()
    '''


time.sleep(5)
# 退出驱动
# browser.close()
# browser.quit()