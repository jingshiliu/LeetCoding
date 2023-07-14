def lowest_common_ancestor(root, p, q):
    # CONDITION 1: self is p or q, if one of descendant is p or q, then it is the res
    # running dfs
    # is the first answer found the lowest?
    # yes, bc if self is p or q and no descendant is the other one, meaning current branch has no other node
    # and no node between the ANS and current node is the other vaonelue, bc that will satisfy the condition 1

    # two situations: self is one node, and one descendant is other one
    # find each one in each subtree (left and right)

    res = None

    def dfs(node):
        nonlocal res
        if not node or res is not None: return False

        find_left = dfs(node.left)
        find_right = dfs(node.right)

        is_self = node == p or node == q
        if (is_self and (find_left or find_right)) or (find_left and find_right):
            res = node
            return False

        return is_self or find_left or find_right

    dfs(root)
    return res


def lowestCommonAncestor(root, p, q):
    if not root: return None

    left_res = lowestCommonAncestor2(root.left, p, q)
    right_res = lowestCommonAncestor2(root.right, p ,q)

    if (left_res and right_res) or (root == p or root == q):
        return root
    return left_res or right_res


def lowestCommonAncestor2(root, p, q):
    res = root
    found_ans = False

    def has_target(node):
        # Assignment to a outer scope variable must add 'nonlocal' keyword
        nonlocal res, found_ans
        if not node or found_ans: return False

        left = has_target(node.left)
        right = has_target(node.right)

        if node.val == p.val or node.val == q.val:
            if left or right:
                res = node
                found_ans = True
            return True

        elif left and right:
            res = node
            found_ans = True

        return left or right

    has_target(root)
    return res


