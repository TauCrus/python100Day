'''
生成“斐波拉切数列”
'''


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


def fib(n):
    a = 0
    b = 1

    for _ in range(n):
        print(a, end=' ')
        a, b = b, a+b


if __name__ == "__main__":

    # 法1
    fib(20)

    print()

    # 法3
    for i in range(20):
        print(fibonacci(i), end=' ')
