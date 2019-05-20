import sys


def main():
    f1 = [x for x in range(1, 10)]
    # print(f1)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    f2 = [x + y for x in 'ABCDE' for y in '1234567']
   # print(f2)
    '''
    ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 
    'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 
    'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 
    'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 
    'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']
    '''

    f3 = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f3))
    # print(f3)

    for v in f3:
        print(v)


if __name__ == "__main__":
    main()
