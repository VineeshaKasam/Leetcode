'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
the nodes of the first two lists.
'''
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def mergeTwoLists(self, l1, l2):

        if not l1 or not l2:
            return l1 or l2
        if l1.val<l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2