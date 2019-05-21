'''
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

'''

row = int(input('请输入行数：'))

# 直角三角形 1
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()

# 直角三角形 2
for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

# 等腰三角形
for i in range(row):
    for j in range(row + i):
        if  row - i <= j + 1 <= row + i :
            print('*', end='')
        else: 
            print(' ', end='')
    print()