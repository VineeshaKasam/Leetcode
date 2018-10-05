'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
'''

class Solution(object):
    def combine(self, n, k):
        result = []
        path = []
        index = 1
        self.dfs(n, k, path, index, result)
        return result

    def dfs(self, n, k, path, index, result):
        if len(path) == k:
            result.append(path)
            return

        for i in range(index, n + 1):
            self.dfs(n, k, path + [i], i + 1, result)
