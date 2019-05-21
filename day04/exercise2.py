'''
输入两个正整数计算最大公约数和最小公倍数
'''

x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x
for f in range(x, 0, -1):
    if x % f == 0 and y % f == 0:
        print('%d和%d的最大公约数是%d' % (x, y, f))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // f))
        break