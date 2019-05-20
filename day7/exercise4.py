# 返回传入的列表中最大和第二大的元素


def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])

    for index in range(2, len(x)):
        print("m1:", m1, " m2:", m2, " x[index]", x[index])
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]

    return m1, m2


if __name__ == "__main__":
    x = [1, 3, 5, 6, 7, 8, 3]
    print(max2(x))
