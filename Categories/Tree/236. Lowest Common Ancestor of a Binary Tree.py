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


