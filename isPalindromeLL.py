'''
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        strs = []
        while head:
            strs.append(head.val)
            head = head.next

        if strs == [] or len(strs) == 1:
            return True
        i = 0
        j = len(strs) - 1
        while i <= len(strs) / 2:
            if strs[i] != strs[j]:
                return False
            i += 1
            j -= 1

        return True

