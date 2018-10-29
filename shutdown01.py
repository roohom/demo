# coding:utf-8

from PyQt5 import QtWidgets,QtGui,QtCore
import sys
import datetime
import subprocess
import imgs
'''
    自动关机小工具
'''
class MainUi(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.init_ui()
        self.timer_status = False

    def init_ui(self):
        self.setWindowTitle('扫雷')   # 窗口标题
        self.setFixedSize(500, 350)  # 窗口初始大小

        # 设置图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":gj.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

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
                        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
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
        self.widget_top_layout.addWidget(self.datetime_label,0,0,1,3)
        self.widget_top_layout.addWidget(self.timer_lable, 1, 0, 1, 3)
        self.widget_top_layout.addWidget(self.attention_img,0,4)

        self.widget_bottom = QtWidgets.QTabWidget()    # 下方选项卡部件
        # 倒计时自动关机
        self.timer_tab = QtWidgets.QTabWidget() # 创建一个选项卡
        self.timer_tab_layout = QtWidgets.QGridLayout() # 创建一个网格布局
        self.timer_tab.setLayout(self.timer_tab_layout) # 设置选项卡布局为网格
        self.timer_10 = QtWidgets.QRadioButton("1") # 创建单选按钮
        self.timer_10.setObjectName('timer_button')
        self.timer_15 = QtWidgets.QRadioButton("2")
        self.timer_10.setObjectName('timer_button')
        self.timer_30 = QtWidgets.QRadioButton("3")
        self.timer_60 = QtWidgets.QRadioButton("6")
        self.timer_60.setChecked(True) # 设置为默认选中
        self.timer_90 = QtWidgets.QRadioButton("9")
        self.timer_custom = QtWidgets.QTimeEdit() # 时间选择输入框
        self.timer_custom.setDisplayFormat("HH:mm:ss") # 设置时间选择框格式
        self.timer_shutdown = QtWidgets.QPushButton("开始扫雷")
        self.timer_shutdown.clicked.connect(self.start_timer_shutdown)
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
        self.time_shutdown = QtWidgets.QPushButton("指定时间扫雷")
        self.time_shutdown.setObjectName('start_time')
        self.time_shutdown.clicked.connect(self.start_time_shutdown)
        self.sletime_tab_layout.addWidget(self.time_custom,0,0,1,2)
        self.sletime_tab_layout.addWidget(self.time_shutdown,0,2,1,1)

        self.widget_bottom.addTab(self.timer_tab, "倒计时")
        self.widget_bottom.addTab(self.sletime_tab, "选择时间")
        self.main_layout.addWidget(self.widget_top, 0, 0, 1, 1)
        self.main_layout.addWidget(self.widget_bottom, 1, 0, 2, 0)
        self.setCentralWidget(self.main_widget) # 设置UI核心部件为main_widget

        # 实时时间计时器
        self.datetime = QtCore.QTimer()  # 实例化一个计时器
        self.datetime.setInterval(1000)  # 设置计时器间隔1秒
        self.datetime.start()  # 启动计时器
        self.datetime.timeout.connect(self.show_datetime_slots)  # 计时器连接到槽函数更新UI界面时间
        # 倒计时计时器
        self.timer_time = QtCore.QTimer()  # 实例化一个计时器
        self.timer_time.setInterval(1000)

    # 实时显示当前时间
    def show_datetime_slots(self):
        self.datetime_label.setText(datetime.datetime.strftime(datetime.datetime.today(), "%Y-%m-%d %H:%M:%S"))

    # 实时显示倒计时
    def show_timer_slots(self):
        try:
            if self.secound == 0:
                self.timer_time.stop()
                subprocess.call("shutdown /p")
            else:
                self.secound -= 1
                m, s = divmod(self.secound, 60)
                h, m = divmod(m, 60)
                print("%02d:%02d:%02d" % (h, m, s))
                self.timer_lable.setText("你扫到雷了，倒计时：%02d:%02d:%02d 请妥善保存文件" % (h, m, s))
        except Exception as e:
            print(repr(e))

    # 启动倒计时关机
    def start_timer_shutdown(self):
        if self.timer_status is False:
            self.timer_status = True
            self.timer_shutdown.setText("停止扫雷")
            self.timer_10.setEnabled(False)
            self.timer_15.setEnabled(False)
            self.timer_30.setEnabled(False)
            self.timer_60.setEnabled(False)
            self.timer_90.setEnabled(False)
            self.timer_custom.setEnabled(False)
            self.time_custom.setEnabled(False)
            self.time_shutdown.setEnabled(False)
            if self.timer_custom.text() != '00:00:00':
                print("使用自定义时间")
                h, m, s = self.timer_custom.text().strip().split(":")
                self.secound = int(h) * 3600 + int(m) * 60 + int(s)
            else:
                print("使用预设时间")
                if self.timer_10.isChecked() is True:
                    self.secound = int(self.timer_10.text()[:2]) * 0.3
                elif self.timer_15.isChecked() is True:
                    self.secound = int(self.timer_15.text()[:2]) * 0.4
                elif self.timer_30.isChecked() is True:
                    self.secound = int(self.timer_30.text()[:2]) * 0.2
                elif self.timer_60.isChecked() is True:
                    self.secound = int(self.timer_60.text()[:2]) * 0.1
                elif self.timer_90.isChecked() is True:
                    self.secound = int(self.timer_90.text()[:2]) * 0.1

            self.timer_time.start()
            self.timer_time.timeout.connect(self.show_timer_slots)  # 计时器连接到槽函数更新UI界面时间
        else:
            self.timer_status = False
            self.timer_shutdown.setText("开启倒计时")
            self.timer_time.stop() # 停止倒计时计时器
            self.timer_lable.setText("倒计时已停止！")
            # 重新启用选择
            self.timer_10.setEnabled(True)
            self.timer_15.setEnabled(True)
            self.timer_30.setEnabled(True)
            self.timer_60.setEnabled(True)
            self.timer_90.setEnabled(True)
            self.timer_custom.setEnabled(True)
            self.time_custom.setEnabled(True)
            self.time_shutdown.setEnabled(True)

    # 启动指定时间关机
    def start_time_shutdown(self):
        if self.timer_status is False:
            self.timer_status = True
            self.time_shutdown.setText("停止倒计时!")
            self.timer_10.setEnabled(False)
            self.timer_15.setEnabled(False)
            self.timer_30.setEnabled(False)
            self.timer_60.setEnabled(False)
            self.timer_90.setEnabled(False)
            self.timer_custom.setEnabled(False)
            self.time_custom.setEnabled(False)
            self.timer_shutdown.setEnabled(False)
            set_time = datetime.datetime.strptime(self.time_custom.text(),"%Y-%m-%d %H:%M:%S") # 还原设定时间的时间形式
            print(self.time_custom.text())
            time_delta = (set_time - datetime.datetime.today()).total_seconds() # 计算时间差的总秒数
            print(time_delta)
            if int(time_delta) > 0:
                self.secound = time_delta
                self.timer_time.start() # 启动倒计时计时器
                self.timer_time.timeout.connect(self.show_timer_slots)  # 计时器连接到槽函数更新UI界面时间
        else:
            self.timer_status = False
            self.time_shutdown.setText("指定时间扫雷")
            self.timer_time.stop() # 停止倒计时计时器
            self.timer_lable.setText("倒计时已停止！")
            # 重新启用选择
            self.timer_10.setEnabled(True)
            self.timer_15.setEnabled(True)
            self.timer_30.setEnabled(True)
            self.timer_60.setEnabled(True)
            self.timer_90.setEnabled(True)
            self.timer_custom.setEnabled(True)
            self.time_custom.setEnabled(True)
            self.timer_shutdown.setEnabled(True)

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()