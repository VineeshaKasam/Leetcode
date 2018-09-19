'''
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
'''

def getRow(rowIndex):

    pascals = [[1], [1, 1]]

    if rowIndex == 0:
        return pascals[0]
    if rowIndex == 1:
        return pascals[1]

    for loop in range(2, rowIndex + 2):
        pascallist = [1]

        for k in range(0, loop - 2):
            pascallist.append(pascals[len(pascals) - 1][k] + pascals[len(pascals) - 1][k + 1])

        pascallist.append(1)

        pascals.append(pascallist)

    return pascals[rowIndex + 1]

print getRow(5)