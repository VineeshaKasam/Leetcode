'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def buildTree(self, preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.pop(0))

            root = TreeNode(inorder[idx])

            root.left = self.buildTree(preorder, inorder[0:idx])
            root.right = self.buildTree(preorder, inorder[idx + 1:])

            return root