'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.
'''

def lengthOfLastWord(s):
    # remove the spaces from the string
    # then split the words from the string with delimiter as sapce
    # reverse the list of words
    # get the length of the first word in the list
    return len(s.strip().split(" ")[::-1][0])

print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord(""))
