from Tree.TreeNode import TreeNode


class Solution:
    def find_predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.val

    def find_successor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.val

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left or root.right):
                return None
            elif root.right:
                root.val = self.find_successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.find_predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

        return root