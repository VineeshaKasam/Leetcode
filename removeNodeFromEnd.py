'''
Given a linked list, remove the n-th node from the end of list and return its head.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return 0

        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1

        if count == 1:
            return []

        first = count - n
        print first

        if first == 0:
            head = head.next
            return head

        cur = head
        new_count = 0
        while cur:
            if new_count == (first - 1):
                cur.next = cur.next.next
            new_count += 1
            cur = cur.next

        return head










