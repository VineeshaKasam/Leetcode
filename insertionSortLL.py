'''
Sort a linked list using insertion sort.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        cur = dummy = ListNode(0)

        while head is not None:

            if cur and cur.val > head.val:
                cur = dummy

            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, cur.next.next, head = head, cur.next, head.next

        return dummy.next