'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
'''

def sortColors(self, nums):
    i = j = 0

    for k in range(0, len(nums)):
        color = nums[k]
        nums[k] = 2

        if color < 2:
            nums[j] = 1
            j += 1
        if color == 0:
            nums[i] = 0
            i += 1