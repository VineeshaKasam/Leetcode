'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice
and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place
with O(1) extra memory.
'''

def removeDuplicates(self, nums):

    i = 0
    for num in nums:
        if i < 2 or num > nums[i - 2]:
            nums[i] = num
            i += 1
    return i