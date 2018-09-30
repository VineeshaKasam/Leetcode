'''
Given a linked list, swap every two adjacent nodes and return its head.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def swapPairs(self, head):
        pre, pre.next = self, head

        while pre.next and pre.next.next:
            a = pre.next
            b = pre.next.next

            pre.next, a.next, b.next = a.next, b.next, a
            pre = a

        return self.next