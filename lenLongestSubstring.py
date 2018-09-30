'''
Given a string, find the length of the longest substring without repeating characters.
'''

def lengthOfLongestSubstring(s):

    mydict = {}
    result = 0
    start = 0

    for index, char in enumerate(s):
        if char in mydict:
            result = max(result, index - start)
            start = max(start, mydict[char] + 1)
        mydict[char] = index

    return max(result, len(s) - start)