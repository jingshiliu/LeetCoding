def max_level_sum(root):
    """
    Time: O(n)
    Space: O(n) last level has up to N/2 nodes

    BFS
    """
    cur_level, next_level = [root], []
    max_sum, max_level = root.val, 1

    cur_depth = 1
    while cur_level:
        cur_sum = 0
        for node in cur_level:
            cur_sum += node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_level = cur_depth
        cur_depth += 1
        cur_level, next_level = next_level, []

    return max_level