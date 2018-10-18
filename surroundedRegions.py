'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''
from collections import deque

def solve(board):
    queue = deque([])
    print board
    for r in xrange(len(board)):
        for c in xrange(len(board[0])):
            if (r in [0, len(board) - 1] or c in [0, len(board[0]) - 1]) and board[r][c] == "O":
                print r,c
                queue.append((r, c))

    print queue
    while queue:
        r, c = queue.popleft()
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "O":
            print r,c
            board[r][c] = "D"
            queue.append((r - 1, c))
            queue.append((r + 1, c))
            queue.append((r, c - 1))
            queue.append((r, c + 1))

    print board
    for r in xrange(len(board)):
        for c in xrange(len(board[0])):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "D":
                board[r][c] = "O"

solve([["X", "X","X","X"], ["X", "O","O","X"], ["X", "X","O","X"], ["X", "O","X","X"]])
