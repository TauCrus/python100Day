class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')

    test._Test__bar()
    # test.__bar()
    # AttributeError: 'Test' object has no attribute '__bar'

    print(test._Test__foo)
    # print(test.__foo)
    # AttributeError: 'Test' object has no attribute '__foo'


if __name__ == "__main__":
    main()
