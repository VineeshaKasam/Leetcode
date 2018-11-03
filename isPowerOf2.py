'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1
'''

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return

        while n > 1:
            rem = n % 2
            if rem != 0:
                return False
            if n == 2 and rem == 0:
                return True
            n = n / 2

        return False