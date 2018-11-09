'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
'''

class Solution(object):
    def isUgly(self, num):
        if num == 1:
            return True

        if num <= 0:
            return False

        for i in [2, 3, 5]:
            while num % i == 0:
                num = num / i

        return num == 1