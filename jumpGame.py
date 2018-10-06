'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
'''

def canJump(nums):
    max_val = 0
    for i in range(0, len(nums)):
        max_val = max(max_val, i + nums[i])
        if max_val >= len(nums) - 1:
            return True
        if i == max_val:
            break
    return False