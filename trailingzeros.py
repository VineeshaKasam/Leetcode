'''
Given an integer n, return the number of trailing zeroes in n!.
'''

def trailingZeroes(n):
    count = 0
    while n > 0:
        n = n / 5
        count = count + n
    return count

print trailingZeroes(10)