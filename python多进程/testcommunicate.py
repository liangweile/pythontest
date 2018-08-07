# -*-coding:utf-8-*-
from multiprocessing import Process, Queue
#multiprocessing模块提供Queue进程间通信
import os, time, random

def write(q):
    for value in ['A', 'B', 'C']:
        print("put %s to queue"%value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    while True:
        value = q.get(True)
        print("get %s from queue"%value)

if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
