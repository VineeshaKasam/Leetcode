'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
'''
def singleNumber(nums):

    mydict = {}

    for num in nums:
        mydict[num] = mydict.get(num, 0) + 1

    for key, val in mydict.items():
        if val == 1:
            return key

print singleNumber([2,3,1,3,1])