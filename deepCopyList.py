'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the
list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def copyRandomList(self, head):

        mydict = collections.defaultdict(lambda: RandomListNode(0))
        mydict[None] = None

        m = head

        while m:
            mydict[m].label = m.label
            mydict[m].next = mydict[m.next]
            mydict[m].random = mydict[m.random]
            m = m.next

        return mydict[head]