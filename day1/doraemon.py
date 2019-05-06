'''
画哆啦A梦
'''

from turtle import *


def head(x, y):
    # 脑袋
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(320)
    circle(100, -280)
    end_fill()

    # 去掉多余颜色
    color((255, 255, 255), "white")

    penup()
    goto(5, 70)
    setheading(0)
    pendown()
    begin_fill()
    circle(75)
    end_fill()

    # 项圈
    color((0, 0, 0), "red")
    penup()
    goto(70, y)
    pendown()
    begin_fill()
    setheading(180)
    forward(130)
    setheading(270)
    forward(10)
    setheading(0)
    forward(130)
    setheading(90)
    forward(10)
    end_fill()

    # 铃铛
    color((0, 0, 0), "yellow")
    penup()
    goto(0, 100)
    setheading(210)
    pendown()
    begin_fill()
    circle(15)
    end_fill()


def eyes(x, y, z):
    # 眼睛
    color((0, 0, 0), "white")

    penup()
    goto(x, y)
    pendown()
    setheading(0)
    begin_fill()
    a = 0.3
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a += 0.06
        else:
            a -= 0.06
        lt(3)
        fd(a)
    end_fill()

    # 眼珠
    color("black")
    penup()
    setheading(90)
    forward(z)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(6)
    end_fill()

    color("white")
    penup()
    setheading(90)
    forward(z/2)
    setheading(0)
    forward(-1)
    pendown()
    begin_fill()
    circle(1)
    end_fill()


def face(x, y, a, b, c):
    color((0, 0, 0), "white")

    # 脸颊
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    setheading(a)
    begin_fill()
    circle(b, c)
    end_fill()


def nose2(x, y):
    # 画鼻子
    color((0, 0, 0), "red")
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(10)
    circle(10)
    end_fill()

    begin_fill()
    setheading(270)
    forward(80)
    end_fill()


def beard(x, y, z):
    # 胡子
    penup()
    goto(x, y)
    pendown()
    setheading(z)
    forward(60)


def mouse(x, y, a, b, c):
    # 嘴巴
    penup()
    goto(x, y)
    pendown()

    setheading(a)
    circle(b, c)


def setting():
    # 设置参数 2
    pensize(2)
    # 隐藏光标
    hideturtle()

    colormode(255)
    color((0, 0, 0), "#1C86EE")
    setup(500, 900)
    speed(0)


def main():
    # 主函数

    # 画哆啦A梦
    setting()
    head(-60, 100)
    face(-60, 100, 305, 90, -115)
    face(70, 100, 55, 90, 115)
    eyes(-14, 200, 10)
    eyes(24, 200, 10)

    nose2(5, 190)

    beard(-20, 190, 155)
    beard(-20, 170, 180)
    beard(-20, 150, 205)

    beard(30, 190, 25)
    beard(30, 170, 00)
    beard(30, 150, 325)

    mouse(-50, 160, -90, 50, 95)
    mouse(60, 160, 90, 50, -95)

    done()


if __name__ == "__main__":
    main()
