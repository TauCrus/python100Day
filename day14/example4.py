'''
图片服务器
'''

from socket import socket
from base64 import b64encode
from json import dumps
from threading import Thread


def main():
    '''自定义线程类'''
    class FileTransferHandler(Thread):

        def __init__(self, c_client):
            super().__init__()
            self.c_client = c_client

        def run(self):
            my_dict = {}
            my_dict['file_name'] = 'ball.png'
            '''
            JSON是纯文本不能携带二进制数据
            所以图片的二进制数据要处理成base64编码
            '''
            my_dict['file_data'] = data
            '''通过dumps函数将字典处理成JSON字符串'''
            json_str = dumps(my_dict)
            '''发送JSON字符串'''
            self.c_client.send(json_str.encode('utf-8'))
            self.c_client.close()

    server = socket()
    server.bind(('127.0.0.1', 9876))
    server.listen(512)
    print('服务器启动开始监听...')

    with open('ball.png', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        '''启动一个线程来处理客户端的请求'''
        FileTransferHandler(client).start()


if __name__ == "__main__":
    main()
