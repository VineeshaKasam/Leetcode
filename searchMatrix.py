'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        if matrix == [] or matrix == [[]]:
            return False

        r = len(matrix)
        c = len(matrix[0])

        if r == 1 and c == 1:
            return target == matrix[r - 1][c - 1]

        for i in range(0, r):
            if target == matrix[i][0] or target == matrix[i][c - 1]:
                return True
            target_range = range(matrix[i][0], matrix[i][c - 1])
            if target in target_range:
                for value in matrix[i]:
                    if value == target:
                        return True
            elif i == (r - 1):
                break
            else:
                end = matrix[i][c - 1]
                start = matrix[i + 1][0]

                if end < target < start:
                    return False

        return False