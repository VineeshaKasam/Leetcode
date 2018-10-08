'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
segmented into a space-separated sequence of one or more dictionary words.
'''

def wordBreak(s, wordDict):
    dp = [False] * len(s)

    for i in range(0, len(s)):
        for word in wordDict:

            if word == s[i - len(word) + 1:i + 1]:
                if (dp[i - len(word)] or i - len(word) == -1):
                    dp[i] = True
    return dp[-1]