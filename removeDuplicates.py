'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers
from the original list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:

            if head.val == head.next.val:
                while head and head.next and head.next.val == head.val:
                    head = head.next
                head = head.next
                pre.next = head

            else:
                pre = pre.next
                head = head.next

        return dummy.next