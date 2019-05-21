class Student(object):

    # 初始化方法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s在学习%s.' % (self.name, course_name))

    def watch_mv(self):
        if self.age < 18:
            print('%s只能看动画片.' % self.name)
        else:
            print('%s正在看岛国动作片.' % self.name)


def main():
    stu1 = Student('chenqq', 20)
    stu1.study("python入门到放弃")
    stu1.watch_mv()

    stu2 = Student("pzp", 18)
    stu2.study("五年高考三年模拟")
    stu2.watch_mv()


if __name__ == "__main__":
    main()
