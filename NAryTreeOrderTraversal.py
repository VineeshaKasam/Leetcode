'''
Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

    def levelOrder(self, root):
        queue = [root]
        res = []

        while any(queue):
            res.append([node.val for node in queue])

            queue = [child for node in queue for child in node.children if child]

        return res
