def leafSimilar(root1, root2) -> bool:
    """
    Time: O(T1 + T2)
    Space: O(T1, T2)
    """

    def dfs(node, sequence):
        if not node: return
        if not node.left and not node.right:
            sequence.append(node.val)
            return

        dfs(node.left, sequence)
        dfs(node.right, sequence)

    seq1, seq2 = [], []
    dfs(root1, seq1)
    dfs(root2, seq2)
    return tuple(seq1) == tuple(seq2)