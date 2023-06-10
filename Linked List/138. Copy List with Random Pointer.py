# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    """
    Map old node to copied node
    then construct list from the hashmap
    """
    def copyRandomListBetter(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]


    """
    store randomIndex in a list
    then create copied linked list that has no random pointer
    random pointer point to right node
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        listPointers = {}
        randomIndex = []
        cur = head

        i = 0
        while cur:
            listPointers[cur] = i
            cur = cur.next
            i += 1

        cur = head
        while cur:
            if cur.random and cur.random in listPointers:
                randomIndex.append(listPointers[cur.random])
            else:
                randomIndex.append(None)
            cur = cur.next

        curListPointers = []

        def copyList(node, index=0):
            if not node:
                return None
            curNode = Node(node.val)
            curListPointers.append(curNode)
            curNode.next = copyList(node.next, index + 1)
            return curNode

        copyHead = copyList(head)

        cur = copyHead
        i = 0
        while cur:
            if randomIndex[i] is not None:
                cur.random = curListPointers[randomIndex[i]]
            cur = cur.next
            i += 1
        return copyHead
