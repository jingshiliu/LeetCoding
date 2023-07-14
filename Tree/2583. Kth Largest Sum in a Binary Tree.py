from TreeNode import TreeNode

def kth_largest_level_sum(root: TreeNode, k: int) -> int:
    level_sums = []
    cur_level, next_level = [root], []

    while cur_level:
        cur_sum = 0
        for node in cur_level:
            cur_sum += node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level_sums.append(cur_sum)
        cur_level, next_level = next_level, []
    if k > len(level_sums):
        return -1
    level_sums.sort()
    return level_sums[len(level_sums) - k]