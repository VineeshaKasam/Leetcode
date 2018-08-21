'''
Given a 32-bit signed integer, reverse digits of an integer.
'''
def reverse(x):
    flag = 1
    result = 0
    if x < 0:
        x = abs(x)
        flag = -1

    while (x > 0):
        if result > 214748364:
            return 0
        result = result * 10 + x % 10
        x /= 10

    return result * flag

print(reverse(-123))
