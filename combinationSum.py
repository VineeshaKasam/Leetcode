'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique
 combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):

        if target < 0:
            return

        if target == 0:
            res.append(list(path))
            return

        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)