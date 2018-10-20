'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):

        if not head or not head.next or not head.next.next:
            return

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head1, head2 = head, slow.next

        slow.next, cur, pre = None, head2, None

        while cur:
            curnext = cur.next
            cur.next = pre
            pre = cur
            cur = curnext

        cur1 = head1
        cur2 = pre

        while cur2:
            next1, next2 = cur1.next, cur2.next
            cur1.next = cur2
            cur2.next = next1
            cur1, cur2 = next1, next2