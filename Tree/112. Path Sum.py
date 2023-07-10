def has_path_sum(root, target_sum):
    """
    Time: O(n)
    Space: O(n)
    """
    if not root: return False
    def dfs(node, last_sum: int):
        if not node:
            return False

        cur_sum = last_sum + node.val
        if cur_sum == target_sum and not node.left and not node.right:
            return True
        return dfs(node.left, cur_sum) or dfs(node.right, cur_sum)

    return dfs(root, 0)