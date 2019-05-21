class Person(object):

    # 限定Person 对象只能绑定_name,_age,和 _gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    #修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩王者荣耀' % self._name)
        else:
            print('%s正在玩英雄联盟' % self._name)


def main():
    person = Person('王老板', 18)
    person.play()
    person.age = 16
    person.play()

    person._gender = '男'

    # AttributeError: 'Person' object has no attribute '_isrich'
    # person._isrich = True


if __name__ == "__main__":
    main()
