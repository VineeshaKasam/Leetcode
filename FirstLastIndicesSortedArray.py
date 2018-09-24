'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
'''


def searchRange(nums, target):

    if len(nums) == 0:
        return [-1,-1]
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) / 2
        if target> nums[mid]:
            low = mid+1
        elif target< nums[mid]:
            high = mid-1
        else:
            while nums[low]!=target:
                low+=1
            while nums[high]!=target:
                high-=1
            return [low,high]

    return [-1,-1]

print searchRange([5,7,7,8,8,10], 8)