'''
获取网络图片
'''

# from time import time
from threading import Thread

import requests

# 继承Thread类创建自定义的线程类


class DownloadHandler(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        file_name = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/taucrus/' + file_name, 'wb') as f:
            f.write(resp.content)


def main():
    resp = requests.get(
        'http://api.tianapi.com/meinv/?\
            key=78686d0772723d6f6a2c030bf1528273&\
                num=10')

    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        DownloadHandler(url).start()


if __name__ == "__main__":
    main()
