'''
Given a collection of distinct integers, return all possible permutations.
'''

class Solution(object):
    def permute(self, nums):
        path = []
        res = []
        self.dfs(nums, path, res)
        return res


    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(0, len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)