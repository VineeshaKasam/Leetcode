'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''

class Solution(object):
    def rotate(self, nums, k):

        for i in range(0, k):
            last = nums.pop()
            nums.insert(0, last)
