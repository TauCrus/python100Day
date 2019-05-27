'''
继承Thread类 创建线程
'''

from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name

    def run(self):
        print('开始下载%s...' % self._file_name)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成！耗费了%d秒' % (self._file_name, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到精通.pdf')
    t1.start()
    t2 = DownloadTask('MySQL从删库到跑路.txt')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒' % (end - start))


if __name__ == "__main__":
    main()
