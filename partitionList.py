'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than
or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        l1 = h1 = ListNode(0)
        l2 = h2 = ListNode(0)

        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next

        return h1.next