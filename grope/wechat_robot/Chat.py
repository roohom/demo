# -*- coding: utf-8 -*-

import Distance as Distance
import Tuling as Tuling
import NetEaseMusic as NetEaseMusic
import Weather as Weather
import time


def has_music(text):
    if NetEaseMusic.isOpen:
        if "关闭音乐" == text:
            NetEaseMusic.isOpen = False
            return "欢迎下次使用"
        else:
            return NetEaseMusic.query_music_info(text)
    elif '打开音乐' == text:
        NetEaseMusic.isOpen = True
        return NetEaseMusic.HELP_MSG
    else:
        return has_distance(text)


def has_distance(text):
    if Distance.isOpen:
        Distance.isOpen = False
        return "你距离我 %s" % Distance.distance("上海市长宁区凯利大厦", text)
    elif text in ['你在哪', '离我多远', '距离']:
        Distance.isOpen = True
        return Distance.HELP_MSG
    else:
        return has_weather(text)


def has_weather(text):
    if text[-2].__eq__("天") and text[-1].__eq__("气"):
        if text.__contains__("最近"):
            return Weather.get_weather(False, str(text).replace("天气", "").replace("最近", ""))
        elif text.__contains__("一周"):
            return Weather.get_weather(False, str(text).replace("天气", "").replace("一周", ""))
        elif text.__contains__("今日"):
            return Weather.get_weather(True, str(text).replace("天气", "").replace("今日", ""))
    else:
        return no_music_distance(text)


def no_music_distance(text):
    if '功能' in text:
        return Tuling.GONGNENG
    elif '时间' in text or '几点' in text:
        return "现在是北京时间{}".format(time.strftime("%Y-%m-%d %H:%M:%S"))
    elif '吃鸡' in text:
        return '马上来！！'
    elif text in ['？', '?']:
        return '嗯？'
    else:
        reply = Tuling.get_response(text)
        return reply
