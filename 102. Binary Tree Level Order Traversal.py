
# Finding depth and append

def levelOrder(root):
    res = []

    def findDepth(node, depth):
        if not node:
            return
        if depth > len(res):
            res.append([])
        res[depth - 1].append(node.val)
        findDepth(node.left, depth + 1)
        findDepth(node.right, depth + 1)

    findDepth(root, 1)
    return res


# BFS
from collections import deque

def levelOrderBFS(root):
    res = []
    queue = deque()
    if root:
        queue.append(root)
    q = len(queue)
    while q:
        cur = []
        for i in range(q):
            temp = queue.popleft()
            cur.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)

        res.append(cur)
        q = len(queue)

    return res


