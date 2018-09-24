'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
'''

def search(nums, target):
    if len(nums)==0:
        return -1
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low + high) / 2
        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low]<=target<=nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if nums[mid]<=target<=nums[high]:
                low = mid+1
            else:
                high = mid-1
    return -1

print search([4,5,6,7,0,1,2], 0)

