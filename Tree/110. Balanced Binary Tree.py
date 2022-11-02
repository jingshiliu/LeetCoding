# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalancedTree = True

        def getDepth(node):
            if not node:
                return 0
            # if it is unbalanced at a node
            # then, the difference between the depth of left subtree and right subtree larger than 1
            # therefore, we get left, and then right. compare them

            leftDepth = getDepth(node.left)
            rightDepth = getDepth(node.right)
            if abs(leftDepth - rightDepth) > 1:
                nonlocal isBalancedTree
                isBalancedTree = False

            return max(leftDepth, rightDepth) + 1

        getDepth(root)
        return isBalancedTree