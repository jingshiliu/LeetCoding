def lowestCommonAncestor(root, p, q):
    if q.val < p.val:
        return lowestCommonAncestor(root, q, p)

    if (root.val == p.val or root.val == q.val) or (p.val < root.val < q.val):
        return root
    return lowestCommonAncestor(root.left, p, q) if p.val < root.val else lowestCommonAncestor(root.right, p, q)