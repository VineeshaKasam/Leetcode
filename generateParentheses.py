'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

def generateParenthesis(n):

    result = []
    stack = [("(", 1, 0)]
    while stack:

        x, l, r = stack.pop()
        if l - r < 0 or l > n or r > n:
            continue
        if l == n and r == n:
            result.append(x)

        stack.append((x + "(", l + 1, r))
        stack.append((x + ")", l, r + 1))

    return result