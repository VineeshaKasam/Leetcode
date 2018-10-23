'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        ans = []
        level = [root]

        while level:
            temp = []
            for node in level:
                temp.append(node.val)

            ans.append(temp)

            temp_child = []
            for node in level:
                temp_child.extend([node.left, node.right])
            level = [leaf for leaf in temp_child if leaf]

        return ans
