from math import sqrt


class Point(object):
    def __init__(self, x=0, y=0):
        '''
        初始化方法
        param x 横坐标
        param y 纵坐标
        '''
        self.x = x
        self.y = y

    def move_to(self, x, y):
        '''
        移动到指定位置（坐标）
        param x 横坐标
        param y 纵坐标
        '''
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        '''
        移动指定的增量
        param dx 横坐标的增量
        param dy 纵坐标的增量
        '''

        self.x += dx
        self.y += dy

    def distance_to(self, other):
        '''
        计算与另一个点的距离
        param other 另一个点
        '''
        dx = self.x - other.x
        dy = self.y - other.y

        return sqrt(dx ** 2 + dy ** 2)

    def show(self):
        print('坐标为[%d, %d]' % (self.x, self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()

    p1.show()
    p2.show()

    # p1.move_to(13, 6)
    # p1.show()

    p2.move_by(-1, 2)
    p2.show()

    print("距离为：", p1.distance_to(p2))


if __name__ == "__main__":
    main()
