import os
import multiprocessing


def copy_file(q,file_name,old_folder_name,new_folder_name):
    """完成文件的复制"""
    # print("===>模拟copy文件:从 %s ---> 到 %s 文件名是: %s" % (old_folder_name,new_folder_name,file_name))
    old_f = open(old_folder_name + "/" + file_name,"rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name,"wb")
    new_f.write(content)
    new_f.close()

    # 拷贝完成 发送哟个消息到队列
    q.put(file_name)

def main():
    # 1.获取用户要复制的文件夹名字
    old_folder_name = input("请输入要复制的文件名")

    # 2.创建一个新文件夹
    new_folder_name = old_folder_name + "[复件]"
    os.mkdir(new_folder_name)

    # 3.获取文件夹下所有带复制的文件名
    file_names = os.listdir(old_folder_name)

    # 4.创建进程池
    po = multiprocessing.Pool(5)

    # 5. 创建一个队列
    q = multiprocessing.Manager().Queue()

    # .向进程池中添加任务
    for file_name in file_names:
        po.apply_async(copy_file,args=(q,file_name,old_folder_name,new_folder_name))

    po.close()
    # po.join()
    file_num = len(file_names)
    copy_ok = 0
    while True:
        file_name = q.get()
        # print("已经完成 : %s" % file_name)
        copy_ok += 1
        print("\r已经完成进度 : %.2f %%" % (copy_ok*100/file_num),end="")
        if copy_ok >= file_num:
            break
if __name__ == "__main__":
    main()