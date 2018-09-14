'''
Given a column title as appear in an Excel sheet, return its corresponding column number.
'''
def titleToNumber(s):

    result = 0
    if s == "":
        return 0
    else:
        s = s[::-1]
        for i in range(0, len(s)):
            val = ord(s[i]) - ord('A') + 1
            result += val * (26 ** i)

        return result

print titleToNumber("ZY")