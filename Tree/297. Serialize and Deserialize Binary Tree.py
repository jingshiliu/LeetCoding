from Tree.TreeNode import TreeNode


def serialize(root):
    res = []

    def preorder(node):
        if not node:
            res.append('N')
        else:
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    return ' '.join(res)


def deserialize(self, data):
    data = data.split(' ')
    self.i = 0

    def retrieveTree():
        if self.i >= len(data) or data[self.i] == 'N':
            self.i += 1
            return

        node = TreeNode(int(data[self.i]))
        self.i += 1
        node.left = retrieveTree()
        node.right = retrieveTree()

        return node

    return retrieveTree()