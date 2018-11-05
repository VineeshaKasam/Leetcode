'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Recursive approach
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def reverseList(self, head):

        pre = None
        return self.reverse(head, pre)


    def reverse(self, node, pre):
        if not node:
            return pre
        n = node.next
        node.next = pre

        self.reverse(n, node)
