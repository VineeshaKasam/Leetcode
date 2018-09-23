'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head

        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        k = k % count

        for i in range(k):
            move = head
            for j in range(count - 2):
                move = move.next
            move.next.next = head
            head = move.next
            move.next = None

        return head
