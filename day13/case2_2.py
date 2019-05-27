# coding:utf-8

'''
使用多进程对复杂任务进行 分而治之 
'''


from multiprocessing import Process, Queue
# from random import randint
from time import time


def task_handler(current_list, result_queue):
    total = 0
    for number in current_list:
        total += number
    result_queue.put(total)


def main():
    processes = []
    result_queue = Queue()
    number_list = [x for x in range(1, 100000001)]
    index = 0
    # 启动8个进程将数据切片后进行运算
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(number_list[index:index + 12500000],
                          result_queue))
        index += 12500000
        processes.append(p)
        p.start()
    # 开始记录所有进程执行完成花费的时间
    start = time()
    for p in processes:
        p.join()
    # 合并执行的结果
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Execution time:%.3fs' % (end-start))


if __name__ == "__main__":
    main()
