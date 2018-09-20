from gevent import monkey
import time
import gevent
import random


# 将程序中用到的耗时操作的代码, 换做 gevent 中自己实现的模块
monkey.patch_all()


def f1(name):
    for i in range(5):
        print(name,i)
        time.sleep(random.random())

def f2(name):
    for i in range(5):
        print(name,i)
        time.sleep(random.random())

gevent.joinall([
    gevent.spawn(f1,"work1"),
    gevent.spawn(f2,"work2")
])




# def f3(n):
#     for i in range(n):
#         print(gevent.getcurrent(),i)
#         time.sleep(random.random())


# print("---1---")
# g1 = gevent.spawn(f1, 5)
# print("---2---")
# g2 = gevent.spawn(f2, 5)
# print("---3---")
# g3 = gevent.spawn(f3, 5)
# print("---4---")
# g1.join()
# g2.join()
# g3.join()