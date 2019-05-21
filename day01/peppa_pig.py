'''
画小猪佩奇
'''

from turtle import *


def nose(x, y):
    # 画鼻子
    penup()
    # 定位到指定坐标
    goto(x, y)
    pendown()
    # 设置海龟（画笔）绘画的方向
    # （0-东、90-北、180-西、270-南）
    setheading(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08

        else:
            a = a - 0.08
        # 向左转3度
        left(3)
        # 向前走（开始画）
        forward(a)
    end_fill()

    # 画鼻孔  1
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    # 设置画笔的颜色
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()

    # 画鼻孔  2
    penup()
    setheading(0)
    forward(20)
    pendown()
    # 设置画笔的颜色
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def head(x, y):
    # 画头
    color((255, 155, 192), "pink")

    # 画轮廓
    penup()
    goto(x, y)
    setheading(0)
    pendown()
    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)

    # 封口
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30:
            a = a + 0.08
        else:
            a = a - 0.08
        # 向左转3度
        lt(3)
        # 向前走（开始画）
        fd(a)

    end_fill()


def ears(x, y):
    # 画耳朵
    color((255, 155, 192), "pink")

    # 第一只耳朵
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()

    # 第二只耳朵
    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()
    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()


def eyes(x, y):
    # 画眼睛 第一只眼睛
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    # 眼珠
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()

    # 画眼睛 第二只眼睛
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-25)
    setheading(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()
    # 眼珠
    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x, y):
    # 画脸颊
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def month(x, y):
    # 画嘴巴
    color((239, 69, 19))
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def setting():
    # 设置参数

    pensize(4)
    # 隐藏光标
    hideturtle()

    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    # speed(10)
    speed(0)


def main():
    # 主函数
    setting()
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    month(-20, 30)
    done()


if __name__ == "__main__":
    main()
