'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right,
level by level from leaf to root).
'''

def levelOrderBottom(self, root):
    if root:
        nodes = [root]
    else:
        nodes = []

    reslist = []
    while len(nodes) > 0:
        reslist.append(list(node.val for node in nodes))
        nodes = [y for nodename in nodes for y in [nodename.left, nodename.right] if y]
    return reslist[::-1]