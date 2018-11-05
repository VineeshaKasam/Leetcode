'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two
characters may map to the same character but a character may map to itself.
'''

class Solution(object):
    def isIsomorphic(self, s, t):
        mydict = {}

        for i in range(0, len(s)):

            if t[i] in mydict.values() and s[i] not in mydict.keys():
                return False

            if s[i] not in mydict.keys():
                mydict[s[i]] = t[i]

            else:
                if mydict[s[i]] != t[i]:
                    return False
        return True