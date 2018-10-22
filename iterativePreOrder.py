'''
Given a binary tree, return the preorder traversal of its nodes' values.

Follow up: Recursive solution is trivial, could you do it iteratively?
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return res