class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# HashMap implementation (best)
def buildTree(preorder, inorder):
    inorderIndex = {n: i for i, n in enumerate(inorder)}  # O(n)

    def build(preorderStart, preorderEnd, inorderStart, inorderEnd):
        if not (preorderEnd > preorderStart or inorderStart < inorderEnd):
            return

        node = TreeNode(preorder[preorderStart])
        mid = inorderIndex[preorder[preorderStart]] - inorderStart

        node.left = build(preorderStart + 1, preorderStart + 1 + mid, inorderStart, inorderStart + mid)
        node.right = build(preorderStart + mid + 1, preorderEnd, inorderStart + mid + 1, inorderEnd)

        return node

    return build(0, len(preorder), 0, len(inorder))


# List Slicing implementation (bad time complexity, but easier to understand, the one above is based on this one)
def buildTreeListSlicing(preorder, inorder):
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = buildTreeListSlicing(preorder[1: 1 + mid], inorder[:mid])
        root.right = buildTreeListSlicing(preorder[mid + 1:], inorder[mid + 1:])

        return root
