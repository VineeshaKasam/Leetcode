'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.

'''


def myAtoi(str_to_convert):
    s = str_to_convert
    if len(s) == 0: return 0

    ls = list(s.strip()) # getting rid of the white spaces

    sign = -1 if ls[0] == '-' else 1 # negative or positive integer

    if ls[0] in ['-', '+']: del ls[0] # deleting the sign
    ret, i = 0, 0

    while i < len(ls) and ls[i].isdigit():
        ret = ret * 10 + ord(ls[i]) - ord('0')
        i += 1
    return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


print(myAtoi("words and 987"))

print(myAtoi("-4237 and remain"))



