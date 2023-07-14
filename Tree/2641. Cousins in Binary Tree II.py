def replace_value_in_tree(root):
    # Time: O(n)
    # Space: O(n)
    # find cur level sum
    # when pushing the node, push the sum of its brother also, so we can get the sum of cousins by subtracting it

    cur_level, next_level = [[root, root.val]], []
    while cur_level:
        level_sum = 0
        # calculate current level sum and push the next level to queue
        for [node, brother_sum] in cur_level:
            level_sum += node.val

            left_val = node.left.val if node.left else 0
            right_val = node.right.val if node.right else 0
            brother_sum = left_val + right_val
            if node.left:
                next_level.append([node.left, brother_sum])
            if node.right:
                next_level.append([node.right, brother_sum])

        # replace the value of current level nodes
        for [node, brother_sum] in cur_level:
            node.val = level_sum - brother_sum

        cur_level, next_level = next_level, []
    return root