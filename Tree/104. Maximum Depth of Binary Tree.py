def maxDepth(root) -> int:
    if not root: return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))




def maxDepth1(root_node) -> int:
    def findMaxDepth(root, depth):
        if not root:
            return depth

        return max(findMaxDepth(root.left, depth + 1), findMaxDepth(root.right, depth + 1))

    return findMaxDepth(root_node, 0)


