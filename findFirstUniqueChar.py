'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

class Solution(object):
    def firstUniqChar(self, s):

        #         for i in range(0,len(s)):
        #             if s.count(s[i])==1:
        #                 return i

        #         return -1

        letters = "abcdefghijklmnopqrstuvwxyz"

        counts = [s.index(l) for l in letters if s.count(l) == 1]

        return min(counts) if len(counts) > 0 else -1