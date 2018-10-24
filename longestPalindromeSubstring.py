'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''

class Solution(object):
    def longestPalindrome(self, s):
        res = ""

        for k in range(0, len(s)):

            strs = self.palindrome(s, k, k)
            if len(strs) > len(res):
                res = strs

            strs = self.palindrome(s, k, k + 1)
            if len(strs) > len(res):
                res = strs

        return res

    def palindrome(self, s, l, r):

        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1:r]