'''
Given an array of size n, find the majority element. The majority element is the element
that appears more than ⌊ n/2 ⌋ times.
'''
def majorityElement(nums):
    numlist = []
    for i in nums:
        if i not in numlist:
            numlist.append(i)

    print numlist
    count = 0
    for k in numlist:
        print nums.count(k), count
        if nums.count(k) > count:
            count = nums.count(k)
            majorElement = k
    return majorElement

print majorityElement([3,2,3])

