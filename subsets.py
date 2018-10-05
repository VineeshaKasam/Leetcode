'''
Given a set of distinct integers, nums, return all possible subsets (the power set).
'''

class Solution(object):
    def subsets(self, nums):
        path = []
        result = []
        self.dfs(nums, path, result)
        return result

    def dfs(self, nums, path, result):
        result.append(path)
        if nums == []:
            return
        for k in range(0, len(nums)):
            self.dfs(nums[k + 1:], path + [nums[k]], result)