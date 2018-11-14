'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
'''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        numlen = len(list(str(num)))
        if numlen == 1:
            return num

        num = list(str(num))
        # print num
        while len(num) > 1:
            sums = 0
            for i in num:
                sums += int(i)

            num = list(str(sums))

        return sums
