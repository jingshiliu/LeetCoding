# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def flatten(root) -> None:
    def flatTree(node):
        if not node: return None
        # if right is null, return left, then self
        # next node or the new right node is its first left child
        # the last node in its left flattened subtree is the rightmost node in the subtree
        rFromLeft = flatTree(node.left)
        rFromRight = flatTree(node.right)

        if node.right:
            if node.left:
                rFromLeft.right = node.right
                node.right = node.left
                node.left = None
            return rFromRight
        if node.left:
            node.right = node.left
            node.left = None
            return rFromLeft
        return node
    flatTree(root)

