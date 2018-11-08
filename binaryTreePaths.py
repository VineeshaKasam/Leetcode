'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):

        if root is None:
            return []
        res = []
        mystack = []

        mystack.append((root, ""))

        while mystack:
            root, path = mystack.pop()

            if root.left is None and root.right is None:
                res.append(path + str(root.val))

            if root.right is not None:
                mystack.append((root.right, path + str(root.val) + "->"))

            if root.left is not None:
                mystack.append((root.left, path + str(root.val) + "->"))

        return res