'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def sumNumbers(self, root):
        if not root:
            return 0

        stack = [(root, root.val)]
        result = 0

        while len(stack) != 0:
            root, root_value = stack.pop()
            if not root.right and not root.left:
                result += root_value
            if root.right:
                stack.append((root.right, root_value * 10 + root.right.val))
            if root.left:
                stack.append((root.left, root_value * 10 + root.left.val))
        return result