def path_sum(root, target_sum):
    """
    Time: O(n2) total N nodes, worst scenario complete binary tree (N/2 leaves), each leaf form a path,
          potentially do a O(n) to copy STATE list to res
    Space: O(n) recursion, and state list
    """
    # state arr stores the current path
    # on find a path, append a copy of state list to res
    res, state = [], []

    def dfs(node, cur_sum):
        if not node: return

        state.append(node.val)
        cur_sum += node.val
        if not node.left and not node.right and cur_sum == target_sum:
            res.append(state.copy())
        dfs(node.left, cur_sum)
        dfs(node.right, cur_sum)
        state.pop()

    dfs(root, 0)
    return res