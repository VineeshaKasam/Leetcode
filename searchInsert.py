'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it
would be if it were inserted in order.
'''

def searchInsert(nums, target):
    mydict = {}
    for k in range(0, len(nums)):
        if target == nums[k]:
            return k
        mydict[nums[k]] = k

    if target not in mydict.keys():
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)

print(searchInsert([1,3,5],5))
print(searchInsert([1,3,5],2))