'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
'''

def generate(numRows):
    pascals = [[1], [1, 1]]
    emptylist = []
    if numRows == 0:
        return emptylist

    if numRows == 1:
        return [pascals[0]]
    if numRows == 2:
        return pascals

    for loop in range(3, numRows + 1):
        pascallist = [1]

        for k in range(0, loop - 2):
            pascallist.append(pascals[len(pascals) - 1][k] + pascals[len(pascals) - 1][k + 1])

        pascallist.append(1)

        pascals.append(pascallist)

    return pascals


print generate(5)