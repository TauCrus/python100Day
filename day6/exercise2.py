def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

'''
for i in range(1000):
    if is_palindrome(i):
        print(i + is_palindrome(i))
'''