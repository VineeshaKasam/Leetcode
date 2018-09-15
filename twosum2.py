'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they
add up to a specific target number.
'''

def twoSum(numbers, target):
    mydict = {}
    for i, num in enumerate(numbers):
        if target - num in mydict:
            return [mydict[target - num] + 1, i + 1]
        mydict[num] = i

print twoSum([2,7,11,13], 9)