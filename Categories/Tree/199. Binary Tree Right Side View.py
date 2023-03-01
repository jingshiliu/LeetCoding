# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def getRightSideView(node, depth):
            if not node:
                return
            if depth > len(res):
                res.append(node.val)
            getRightSideView(node.right, depth + 1)
            getRightSideView(node.left, depth + 1)

        getRightSideView(root, 1)
        return res