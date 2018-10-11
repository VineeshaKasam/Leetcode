'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
'''

class Solution(object):
    def permuteUnique(self, nums):
        path = []
        res = []
        self.dfs(nums, path, res)
        #         #print res
        #         for i in range(0,len(res)):
        #             #print res[i], res[:i]
        #             if res[i] in res[:i]:
        #                 res[i] = True
        #         #print res

        #         return [i for i in res if i!=True]
        return res

    def dfs(self, nums, path, res):
        if not nums:
            if list(path) not in res:
                res.append(list(path))

        for i in range(0, len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)