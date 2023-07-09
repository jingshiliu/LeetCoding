# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def goodNodes(root) -> int:
    def find_good(node, max_asc_val) -> int:
        if node is None: return 0
        cur_max_asc = max(node.val, max_asc_val)

        return int(cur_max_asc == node.val) + find_good(node.left, cur_max_asc) + find_good(node.right, cur_max_asc)

    return find_good(root, root.val)


def goodNodes1(root) -> int:
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

