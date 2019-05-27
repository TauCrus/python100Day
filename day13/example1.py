from random import randint
from time import time, sleep


def download_task(file_name):
    print('开始下载%s...' % file_name)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成！耗费了%d秒' % (file_name, time_to_download))


def main():
    start = time()
    download_task('Python从入门到入土.pdf')
    download_task('Hello Python.mp4')
    end = time()
    print('总共耗费； %.2f秒' % (end-start))


if __name__ == "__main__":
    main()
