'''
Sort a linked list in O(n log n) time using constant space complexity
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        if head is None or head.next is None:
            return head

        mid = self.find_mid(head)
        right = mid.next
        mid.next = None

        return self.merge(self.sortList(head), self.sortList(right))

    def find_mid(self, head):

        slow, fast = head, head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, head1, head2):
        dummy = ListNode(0)
        node = dummy
        while head1 and head2:
            if head1.val < head2.val:
                node.next = head1
                head1 = head1.next
            else:
                node.next = head2
                head2 = head2.next
            node = node.next

        node.next = head1 or head2
        return dummy.next
