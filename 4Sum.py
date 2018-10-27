'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that
a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
'''

class Solution(object):
    def fourSum(self, nums, target):

        def NSum(nums, target, N, res, results):

            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return

            if N == 2:
                l = 0
                r = len(nums) - 1

                while l < r:
                    sums = nums[l] + nums[r]
                    if sums == target:
                        results.append(res + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif sums < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(0, len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        NSum(nums[i + 1:], target - nums[i], N - 1, res + [nums[i]], results)

        results = []
        NSum(sorted(nums), target, 4, [], results)
        return results