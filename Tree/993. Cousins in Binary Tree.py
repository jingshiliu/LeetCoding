from TreeNode import TreeNode

def is_cousins(root: TreeNode, x: int, y: int) -> bool:
    # find x and y nodes first
    # record the info of them
    # break the loop

    info = []  # [parent, level]
    cur_level, next_level = [[root, 0]], []
    depth = 1
    while cur_level:
        for [node, parent] in cur_level:
            if node.val == x or node.val == y:
                info.append([parent, depth])
            if node.left:
                next_level.append([node.left, node.val])
            if node.right:
                next_level.append([node.right, node.val])
        depth += 1
        cur_level, next_level = next_level, []

    n1, n2 = info
    return n1[1] == n2[1] and n1[0] != n2[0]