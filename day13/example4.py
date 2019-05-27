'''
多线程
'''
from random import randint
from threading import Thread
from time import time, sleep


def download(file_name):
    print('开始下载%s...' % file_name)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (file_name, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到入土.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Hello World.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()

    print('总共耗费； %.2f秒' % (end-start))


if __name__ == "__main__":
    main()
