'''
Write a program to find the node at which the intersection of two singly linked lists begins.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):

        # if headA is None and headB is None:
        #     return None

        cura, curb = headA, headB

        listA = 0
        listB = 0
        while cura is not None:
            listA += 1
            cura = cura.next
        while curb is not None:
            listB += 1
            curb = curb.next

        cura, curb = headA, headB

        # incrementing the respective pointer by the length difference
        if listB > listA:
            for i in range(listB - listA):
                curb = curb.next

        if listA > listB:
            for i in range(listA - listB):
                cura = cura.next

        while cura != curb:
            cura = cura.next
            curb = curb.next
        return cura # can return curb as well



