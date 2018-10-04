'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?
'''

def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid:
        return
    r, c = len(obstacleGrid), len(obstacleGrid[0])
    obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
    for i in xrange(1, r):
        obstacleGrid[i][0] = obstacleGrid[i - 1][0] * (1 - obstacleGrid[i][0])
    for i in xrange(1, c):
        obstacleGrid[0][i] = obstacleGrid[0][i - 1] * (1 - obstacleGrid[0][i])
    for i in xrange(1, r):
        for j in xrange(1, c):
            obstacleGrid[i][j] = (obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]) * (1 - obstacleGrid[i][j])
    return obstacleGrid[-1][-1]
