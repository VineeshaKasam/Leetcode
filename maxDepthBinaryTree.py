# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):

        # node = root
        # while node.left!=None or node.right!=None:
        #     if node.left!=None:
        #         return 1+self.maxDepth(node.left)
        #         node = node.left
        #     elif node.right!=None:
        #         return 1+self.maxDepth(node.right)
        #         node = node.right
        #     else:
        #         return 0

        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))