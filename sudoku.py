class Solution:

    def isValidSudoku(self, board):
        return self.rowValid(self,board) and self.colValid(self,board) and self.squareValid(self,board)

    def rowValid(self,board):
        for row in board:
            if not self.unitValid(row):
                return False
        return True

    def colValid(self,board):
        for col in zip(*board):
            if not self.unitValid(col):
                return False
        return True

    def squareValid(selfself,board):
        for i in [0,3,6]:
            for j in [0,3,6]:
                square = [board[x][y] for x in range(i, i+3) for y in range(j,j+3)]
                if not self.unitValid(square):
                    return False
        return True

    def unitValid(self, values):
        not_dot = [i for i in values if i != '.']
        return len(set(values))==len(not_dot)

