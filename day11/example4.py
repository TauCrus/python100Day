# 读写二进制文件


def main():
    try:
        with open('ball.png', 'rb') as fs1:
            data = fs1.read()
            print(type(data))

        with open('球.png', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定文件无法打开。', e)
    except IOError as e:
        print('读写文件时出现错误。', e)
    print('程序执行结束。')


if __name__ == "__main__":
    main()
