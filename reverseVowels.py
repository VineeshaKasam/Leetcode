'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
'''

class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowels.extend(["A", "E", "I", "O", "U"])

        i = 0
        j = len(s) - 1
        s = list(s)

        while i < j:

            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

            elif s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1

        return "".join(s)