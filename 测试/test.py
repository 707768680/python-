# 查找某文件夹下含关键字的文件
# import os

# def search(path,des):
#     for item in os.listdir(path):
#         absfile = os.path.join(path,item)
#         if os.path.isfile(absfile):
#             if item.find(des) != -1:
#                 print(absfile)
#         else:
#             search(absfile,des)
# # if __name__ == 'main':
# search(r'F:\www\python','.py')


# 线程池
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')


# ThreadLocal用法
# import threading
# local_num = threading.local()
# def change_it(n):
#     local_num.balance = local_num.balance + n
#     local_num.balance = local_num.balance - n
#     print(local_num.balance)
# def run_thread(n):
#     local_num.balance = 0
#     for i in range(10):
#         change_it(n)
# t1 = threading.Thread(target=run_thread,args=(5,))
# t2 = threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

