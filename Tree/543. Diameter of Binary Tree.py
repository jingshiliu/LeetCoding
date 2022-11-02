# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def computeRadius(node):
            if not node:
                return 0
            nonlocal diameter

            leftRadius = computeRadius(node.left)
            rightRadius = computeRadius(node.right)
            diameter = max(leftRadius + rightRadius, diameter)

            return max(leftRadius, rightRadius) + 1

        computeRadius(root)

        return diameter