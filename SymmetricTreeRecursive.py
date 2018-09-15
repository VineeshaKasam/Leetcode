'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''

#Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):

        def isSym(L, R):

            if L and R and L.val == R.val:
                return isSym(L.left,R.right) and isSym(L.right, R.left)
            return L == R

        return not root or isSym(root.left, root.right)
