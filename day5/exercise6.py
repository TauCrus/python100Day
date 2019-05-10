'''
摇豹子
'''

from random import randint


count = 0

# bz_count = 0
# b1_count = 0

# for _ in range(1000):
while True:
    a = randint(1, 6)
    b = randint(1, 6)
    c = randint(1, 6)
    d = randint(1, 6)
    e = randint(1, 6)

    count += 1

    if a == b == c == d == e:
        if a == 1:
            # b1_count += 1
            print('摇到5个1 boom')
        else:
            # bz_count += 1
            print('摇到豹子')
        break
print('count:', count)

# print('bz_count:', bz_count)
# print('b1_count:', b1_count)
