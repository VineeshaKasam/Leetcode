'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).
'''

def rotate(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for r in range(0, row):
        for c in range(0, col):

            if r < c:
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for row in matrix:
        row.reverse()
    return matrix

print rotate([[1,2,3], [4,5,6], [7,8,9]])