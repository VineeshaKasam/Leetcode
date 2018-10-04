'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.
'''


def threeSum(nums):
    result = []
    nums.sort()

    for i in range(0, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1

        while l < r:
            sums = nums[i] + nums[l] + nums[r]
            if sums > 0:
                r = r - 1
            elif sums < 0:
                l = l + 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l = l + 1
                while l < r and nums[r] == nums[r - 1]:
                    r = r - 1
                l += 1
                r -= 1
    return result