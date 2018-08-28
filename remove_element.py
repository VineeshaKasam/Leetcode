'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
'''


def removeElement(nums, val):

    for x in nums[:]: # slicing; making a shallow copy (just a reference)
        if x == val:
            nums.remove(x)

    return len(nums)


print(removeElement([2,2,3,5,7,8,2,2],2))