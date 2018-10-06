'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A
gray code sequence must begin with 0.
'''

def grayCode(self, n):
    res = [0]
    for k in range(0, n):
        for value in reversed(res):
            res.append(value + 2 ** k)
    return res