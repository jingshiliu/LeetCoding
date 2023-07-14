from Tree.TreeNode import TreeNode


def search_BST(root: TreeNode, val: int) -> TreeNode:
    cur = root
    while cur:
        if cur.val > val:
            cur = cur.left
        elif cur.val < val:
            cur = cur.right
        else:
            return cur