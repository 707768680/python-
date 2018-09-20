import multiprocessing


def download_from_web(q):
    """下载数据"""
    data = list()
    data = [11,22,33,44]
    for temp in data:
        q.put(temp)
    print("数据已传入队列中")

def analysis_data(q):
    """数据处理"""
    waitting_analysis_data = list()
    while True:
        data = q.get()
        waitting_analysis_data.append(data)
        if q.empty():
            break
    print(waitting_analysis_data)

def main():
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=download_from_web,args=(q,))
    p2 = multiprocessing.Process(target=analysis_data,args=(q,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()