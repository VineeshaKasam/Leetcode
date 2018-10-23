'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
to left for the next level and alternate between).
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def zigzagLevelOrder(self, root):

        if not root:
            return []
        ans = []
        level = [root]

        i = 0
        while level:
            temp = []
            for node in level:
                temp.append(node.val)

            if i % 2 == 0:
                ans.append(temp)
            else:
                ans.append(temp[::-1])

            temp_child = []
            for node in level:
                temp_child.extend([node.left, node.right])

            level = [leaf for leaf in temp_child if leaf]
            i += 1

        return ans
