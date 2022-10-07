# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         slow = fast = head
#         diff = 0
#         while fast.next != None:
#             if diff < n:
#                 diff += 1
#             else:
#                 slow = slow.next

#             fast = fast.next

#         # This covers the cases that slow is the node that need to be removed
#         # because slow points to the node before the node need to be removed ideally
#         # but slow will be the node if n == size of linked list
#         # Time Complexity: O(n)
#         # Space Complexity: O(1)

#         if diff == n - 1:
#             return head.next
#         else:
#             slow.next = slow.next.next

#         return head


# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         def removeNth(node):
#             if node.next == None:
#                 return 0
#             currentPos = 1 + removeNth(node.next)
#             if currentPos == n:
#                 node.next = node.next.next
#             return currentPos


#         if removeNth(head) < n:
#             return head.next
#         return head


def removeNthFromEnd(head, n: int):
    fast, fastIndex, slow, slowIndex = head, 0, head, 0

    while fast.next and fast.next.next:
        fast = fast.next.next
        fastIndex += 2

        slow = slow.next
        slowIndex += 1

    res = head
    resIndex = 0

    if fast.next == None:
        resIndex = fastIndex + 1 - n
    elif fast.next.next == None:
        resIndex = fastIndex + 1 - n + 1

    if slowIndex >= resIndex:
        for i in range(resIndex - 1):
            res = res.next
    else:
        res = slow
        for i in range(resIndex - slowIndex - 1):
            res = res.next

    if resIndex == 0:
        return head.next
    else:
        res.next = res.next.next

    return head

def removeNthFromEnd( head, n: int):
    fast, slow = head, head

    for i in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast, slow = fast.next, slow.next

    slow.next = slow.next.next

    return head
