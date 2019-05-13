# coding=utf8

from exercise2 import is_palindrome
from exercise3 import is_prime

if __name__ == "__main__":
    num = int(input('请输入一个整数：'))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
