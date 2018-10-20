'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
'''

class Solution(object):
    def partition(self, s):
        result = []
        path = []
        self.dfs(s, path, result)
        return result

    def dfs(self, s, path, result):

        if not s:
            result.append(path)
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path + [s[:i]], result)

    def isPalindrome(self, s):
        return s == s[::-1]