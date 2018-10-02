'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
'''

def numTrees(self, n):

    dp = {k: 0 for k in range(0, n + 1)}

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    if n < 3:
        return dp[n]

    for nodenum in range(3, n + 1):
        for root in range(1, nodenum + 1):
            dp[nodenum] += dp[root - 1] * dp[nodenum - root]

    return dp[n]