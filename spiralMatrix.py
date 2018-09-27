'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''

def spiralOrder(matrix):

    if not matrix or not matrix[0]:
        return []
    rf = 0
    re = len(matrix)-1

    cf = 0
    ce = len(matrix[0])-1

    res = []
    while rf<re and cf<ce:
        res.extend([matrix[rf][j] for j in range(cf,ce)])
        res.extend([matrix[i][ce] for i in range(rf, re)])
        res.extend([matrix[re][j] for j in range(ce, cf,-1)])
        res.extend([matrix[i][rf] for i in range(re, rf, -1)])
        rf+=1
        cf+=1
        ce-=1
        re-=1

    if rf == re:
        res.extend([matrix[rf][j] for j in range(cf, ce+1)])
    elif cf==ce:
        res.extend([matrix[i][cf] for i in range(rf, re+1)])

    return res