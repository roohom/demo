import ftplib
import os
import socket

HOST = "ftp.acc.umu.se"
DIR = "Public/EFLIB"
FILE = 'README'

try:
    f = ftplib.FTP()
    f.set_debuglevel(2)
    f.connect(HOST)
except Exception as e:
    print(e)
    exit()
print("***Connect to HOST {}".format(HOST))

try:
    f.cwd(DIR)
except Exception as e:
    print(e)
    exit()
print("***Changed dir to {}".format(DIR))

try:
    f.retrbinary("RETR {}".format(FILE),open(FILE,"Wb").write)
except Exception as e:
    print(e)
    exit()


f.quit()
