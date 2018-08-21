'''

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

'''


def twoSum(nums, target):
    mydict = {}

    for k in range(0, len(nums)):

        if target - nums[k] in mydict.keys():
            return [mydict[target - nums[k]], k]
        else:
            mydict[nums[k]] = k

    return 0

print(twoSum([2,7,8,11],9))