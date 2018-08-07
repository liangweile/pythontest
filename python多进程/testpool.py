# -*-coding:utf-8-*-
from multiprocessing import Pool
# 进程池方式创建进程
import os, time, random


def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end - start)))


if __name__ == "__main__":
    print("Parent process %s." % os.getid())
    p = Pool()  # p = Pool(5)同时进行5个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))  # 批量创建进程
    print("Waiting for all subprocesses done")
    p.close()
    p.join()
    print("All subprocesses done")
