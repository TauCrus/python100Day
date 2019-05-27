'''
图片下载客户端
'''

from socket import socket
from json import loads
from base64 import b64decode


def main():
    client = socket()
    client.connect(('127.0.0.1', 9876))
    '''定义一个保存二进制数据的对象'''
    in_data = bytes()
    '''
    由于不知道服务器发送的数据有多大
    每次接收1024字节
    '''
    data = client.recv(1024)
    while data:
        '''将收到的数据拼接起来'''
        in_data += data
        data = client.recv(1024)

    '''
    将收到的二进制数据解码成JSON字符串并转换成字典
    loads函数的作用就是将JSON字符串转换成字典对象
    '''
    my_dict = loads(in_data.decode('utf-8'))
    file_name = my_dict['file_name']
    file_data = my_dict['file_data'].encode('utf-8')

    with open('/Users/taucrus/Downloads/' + file_name, 'wb') as f:
        '''将base64格式的数据解码成二进制数据并写入文件'''
        f.write(b64decode(file_data))
    print('图片已保存.')


if __name__ == "__main__":
    main()
