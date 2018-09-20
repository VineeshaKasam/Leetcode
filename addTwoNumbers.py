'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
 and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
'''

# Definition for singly-linked list.

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None
    def addTwoNumbers(self, l1, l2):

        astr = ''
        bstr = ''

        while l1 is not None:
            astr += str(l1.val)
            l1 = l1.next

        while l2 is not None:
            bstr += str(l2.val)
            l2 = l2.next

        ret = ListNode(0)
        cur = ret
        for k in str(int(astr[::-1]) + int(bstr[::-1]))[::-1]:
            cur.next = ListNode(k)
            cur = cur.next

        return ret.next
