'''
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):

        while head is not None and head.val == val:
            head = head.next
        cur = head

        while cur is not None:
            if cur.next is not None and cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head
