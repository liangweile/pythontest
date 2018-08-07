# -*-coding:utf-8-*-
# filename:multiprocessing.py
# !/usr/bin/python2.7
from multiprocessing import Process
# 从multiprocessing模块提供的Process类创建进程对象
import os


# 系统模块

def run_proc(name):
    print("Run child process %s(%s)..." % (name, os.getpid()))  # 当前进程id


if __name__ == "__main__":
    print("Parent process %s" % os.getpid())
    p = Process(target=run_proc, args=('test',))  # args是传入list
    print("Process will start")
    p.start()
    p.join()  # 等待进程结束后继续
    print("Process end")
