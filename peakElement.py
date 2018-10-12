'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

'''
def findPeakElement(nums):

    # return nums.index(max(nums))

    left = 0
    right = len(nums) - 1

    while left < right - 1:
        mid = (left + right) / 2

        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            return mid

        if nums[mid] < nums[mid - 1]:
            right = mid - 1
        else:
            left = mid + 1

    return left if nums[left] >= nums[right] else right