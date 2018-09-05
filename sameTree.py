'''
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''


def isSameTree(self, p, q):
    if p and q:
        root_bool = (p.val == q.val)
        left_bool = self.isSameTree(p.left, q.left)
        right_bool = self.isSameTree(p.right, q.right)
        return root_bool and left_bool and right_bool
    return p is q

