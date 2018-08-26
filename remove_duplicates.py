'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''


def removeDuplicates(nums):
    if len(nums) < 2:
        return len(nums)

    pre = 0
    for cur in range(1, len(nums)):
        if nums[cur] != nums[pre]:
            pre += 1
            nums[pre] = nums[cur]

    return pre + 1


print(removeDuplicates([1,2,2,3,3]))
print(removeDuplicates([0,1,1,1,1,1,2,3,3,3,3,3,3]))
