'''
Given a binary tree, return the inorder traversal of its nodes' values.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def inorderTraversal(self, root):
        result = []
        self.inorder(root, result)
        return result

    def inorder(self, root, result):
        if root is None:
            return
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)
