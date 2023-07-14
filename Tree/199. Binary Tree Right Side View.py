# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def right_side_view(root) -> list[int]:
    """
    Time: O(n)
    Space: O(n)
    """
    res = []

    def dfs(node, depth):
        if not node: return
        if depth > len(res):
            res.append(node.val)

        dfs(node.right, depth + 1)
        dfs(node.left, depth + 1)

    dfs(root, 1)
    return res


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