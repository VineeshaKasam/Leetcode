'''
Given an integer, write a function to determine if it is a power of three.
'''

import math
def isPowerOfThree(n):
    if n <= 0:
        return False
    temp = math.log10(n) / math.log10(3)
    if temp.is_integer():
        return True
    return False