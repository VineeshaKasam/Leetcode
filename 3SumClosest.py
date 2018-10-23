'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()

        res = nums[0] + nums[1] + nums[2]

        for i in range(0, len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sums = nums[i] + nums[j] + nums[k]

                if sums == target:
                    return sums

                if abs(sums - target) < abs(res - target):
                    res = sums

                if sums < target:
                    j += 1
                if sums > target:
                    k -= 1

        return res