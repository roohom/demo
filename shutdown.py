#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : shutdown.py
# Author: roohom
# Date  : 2018/10/27 0027

from PyQt5 import QtWidgets,QtGui,QtCore
import sys
import datetime
import subprocess

'''

    自动关机小工具

'''


class MainUi(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super().__init__()
        self.init_ui()
        self.timer_status = False

    def init_ui(self):
        self.setWindowTitle('自动关机助手 - 州的先生zmister.com')  # 窗口标题
        self.setFixedSize(1000, 500)  # 窗口初始大小
        # 主窗口部件
        self.main_widget = QtWidgets.QWidget() # 实例化一个QWidget部件，作为主窗口的部件
        self.main_widget.setObjectName('main_widget')
        self.main_layout = QtWidgets.QGridLayout() # 创建一个网格布局
        self.main_widget.setLayout(self.main_layout) # 设置主部件的布局为网格布局
        self.setStyleSheet('''
                    #datetime_label{
                        font-size:20px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                    }
                    #at_icon{
                        background-image: url(./alogo.png);
                        width:175px;
                        height:70px;
                    }
                    #start_timer,#start_time{
                        width:40px;
                        height:40px;
                        border:3px solid black;
                        border-radius:10px
                    }
                    #timer_custom_input{
                        width:5px;
                    }
                    #timer_lable{
                        color:red;
                        font-size:16px;
                        font-weight:700;
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif
                    }
                    QTabBar::tab{
                        min-width:40ex;
                        min-height:10ex;
                    }
                ''')

        # 两个子部件
        self.widget_top = QtWidgets.QWidget()   # 上方部件
        self.widget_top_layout = QtWidgets.QGridLayout() # 创建一个网格布局
        self.widget_top.setLayout(self.widget_top_layout) # 设置widget_top布局为网格布局
        self.datetime_label = QtWidgets.QLabel()    # 创建一个日期时间文本
        self.datetime_label.setObjectName('datetime_label')
        self.datetime_label.setText(datetime.datetime.strftime(datetime.datetime.today(),"%Y-%m-%d %H:%M:%S")) # 设置文本内容为当前时间
        self.timer_lable = QtWidgets.QLabel() # 倒计时文本
        self.timer_lable.setObjectName('timer_lable')
        self.shutdown_lable = QtWidgets.QLabel() # 用于显示关机时间
        # 图片按钮
        self.attention_img = QtWidgets.QPushButton() # 创建一个按钮
        self.attention_img.setObjectName('at_icon')
        # 将小部件添加到上层布局中
        self.widget_top_layout.addWidget(self.datetime_label, 0, 0, 1, 3)
        self.widget_top_layout.addWidget(self.timer_lable, 1, 0, 1, 3)
        self.widget_top_layout.addWidget(self.attention_img,0,4)
        self.widget_bottom = QtWidgets.QTabWidget()    # 下方选项卡部件
        # 倒计时自动关机
        self.timer_tab = QtWidgets.QTabWidget() # 创建一个选项卡
        self.timer_tab_layout = QtWidgets.QGridLayout() # 创建一个网格布局
        self.timer_tab.setLayout(self.timer_tab_layout) # 设置选项卡布局为网格
        self.timer_10 = QtWidgets.QRadioButton("10分钟") # 创建单选按钮
        self.timer_10.setObjectName('timer_button')
        self.timer_15 = QtWidgets.QRadioButton("15分钟")
        self.timer_10.setObjectName('timer_button')
        self.timer_30 = QtWidgets.QRadioButton("30分钟")
        self.timer_60 = QtWidgets.QRadioButton("60分钟")
        self.timer_60.setChecked(True) # 设置为默认选中
        self.timer_90 = QtWidgets.QRadioButton("90分钟")
        self.timer_custom = QtWidgets.QTimeEdit() # 时间选择输入框
        self.timer_custom.setDisplayFormat("HH:mm:ss") # 设置时间选择框格式
        self.timer_shutdown = QtWidgets.QPushButton("启动倒计时")
        self.timer_shutdown.setObjectName("start_timer")
        self.timer_tab_layout.addWidget(self.timer_10,0,0)
        self.timer_tab_layout.addWidget(self.timer_15, 0, 1)
        self.timer_tab_layout.addWidget(self.timer_30, 1, 0)
        self.timer_tab_layout.addWidget(self.timer_60, 1, 1)
        self.timer_tab_layout.addWidget(self.timer_90, 2, 0)
        self.timer_tab_layout.addWidget(self.timer_custom, 2, 1,1,1)
        self.timer_tab_layout.addWidget(self.timer_shutdown, 0, 3,3,1)
        # 选择日期时间进行关机
        self.sletime_tab = QtWidgets.QTabWidget()
        self.sletime_tab_layout = QtWidgets.QGridLayout()
        self.sletime_tab.setLayout(self.sletime_tab_layout)
        self.time_custom = QtWidgets.QDateTimeEdit() # 选择时间关机
        self.time_custom.setDateTime(datetime.datetime.today())
        self.time_custom.setDisplayFormat("yyyy-MM-dd HH:mm:ss")  # 设置时间选择框格式
        self.time_shutdown = QtWidgets.QPushButton("指定时间关机")
        self.time_shutdown.setObjectName('start_time')
        self.sletime_tab_layout.addWidget(self.time_custom,0,0,1,2)
        self.sletime_tab_layout.addWidget(self.time_shutdown,0,2,1,1)
        self.widget_bottom.addTab(self.timer_tab,"倒计时关机")
        self.widget_bottom.addTab(self.sletime_tab,"选择时间关机")
        self.main_layout.addWidget(self.widget_top,0,0,1,1)
        self.main_layout.addWidget(self.widget_bottom, 1, 0, 2, 0)
        self.setCentralWidget(self.main_widget) # 设置UI核心部件为main_widget
        # 实时时间计时器
        self.datetime = QtCore.QTimer()  # 实例化一个计时器
        self.datetime.setInterval(1000)  # 设置计时器间隔1秒
        self.datetime.start()  # 启动计时器
        self.datetime.timeout.connect(self.show_datetime_slots)  # 计时器连接到槽函数更新UI界面时间
        # 实时显示当前时间
        def show_datetime_slots(self):
            self.datetime_label.setText(datetime.datetime.strftime(datetime.datetime.today(), "%Y-%m-%d %H:%M:%S"))


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()