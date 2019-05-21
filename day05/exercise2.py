'''
寻找“完美数”

它所有的真因子(即除了自身以外的约数)的和(即因子函数)
恰好等于它本身
'''

import time
import math

# start = time.clock()
start = time.perf_counter()

for num in range(1, 10000):
    sum = 0 
    for factor in range(1, int(math.sqrt(num)) + 1):
        if num % factor == 0:
            sum += factor
            if factor > 1 and num / factor != factor:
                sum += num / factor   
    if sum == num:
        print(num)

# end = time.clock()
end = time.perf_counter()
print('执行时间：', (end - start),'秒')