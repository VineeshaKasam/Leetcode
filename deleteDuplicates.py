'''
Given a sorted linked list, delete all duplicates such that each element appear only once.
'''

def DeleteDuplicates(head):

    cur = head
    while cur:
        while cur.next and cur.next.value==cur.value:
            cur.next = cur.next.next
        cur = cur.next

    return head

