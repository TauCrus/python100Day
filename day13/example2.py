from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(file_name):
    print('启动下载进程，进程号[%d].' % getpid())
    print('开始下载%s...' % file_name)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (file_name, time_to_download))


def main():
    start = time()
    p1 = Process(target=download_task, args=('python从入门到放弃.pdf',))
    p1.start()
    p2 = Process(target=download_task, args=('Hello py.mp3',))
    p2.start()

    p1.join()
    p2.join()
    end = time()
    print('总共耗费了%.2f秒' % (end - start))


if __name__ == "__main__":
    main()
