# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def findGood(node, maxNode):
            if not node:
                return

            if node.val >= maxNode:
                nonlocal res
                res += 1
                findGood(node.left, node.val)
                findGood(node.right, node.val)
            else:
                findGood(node.left, maxNode)
                findGood(node.right, maxNode)

        findGood(root, root.val)
        return res

