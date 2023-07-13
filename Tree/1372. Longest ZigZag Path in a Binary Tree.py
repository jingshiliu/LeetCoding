def longest_zig_zag(root):
    """
    Time: O(n) beats 80%
    Space: O(n) beats 45%
    """

    res = 0

    def dfs(node, went_left, last_length):
        if not node: return

        cur_length = last_length + 1
        nonlocal res
        res = max(res, cur_length)

        if went_left:
            dfs(node.left, True, 0)
            dfs(node.right, False, cur_length)
        else:
            dfs(node.left, True, cur_length)
            dfs(node.right, False, 0)

    dfs(root.left, True, 0)
    dfs(root.right, False, 0)
    return res


def longest_zig_zag1(root):
    """
    Time: O(n)
    Space: O(n)
    """

    res = 0

    def dfs(node, last_direction, last_length):
        if not node: return

        cur_length = last_length + 1
        nonlocal res
        res = max(res, cur_length)

        if last_direction == 'left':
            dfs(node.left, 'left', 0)
            dfs(node.right, 'right', cur_length)
        elif last_direction == 'right':
            dfs(node.left, 'left', cur_length)
            dfs(node.right, 'right', 0)
        else:
            dfs(node.left, 'left', 0)
            dfs(node.right, 'right', 0)

    dfs(root, '', -1)
    return res