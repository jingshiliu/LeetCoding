def deleteMiddle(head):
    """
    Time: O(n)
    Space: O(1)
    """
    if not head.next: return None
    length = 0
    ptr = head
    while ptr:
        length += 1
        ptr = ptr.next

    ptr = head
    for i in range(length // 2 - 1):
        ptr = ptr.next

    ptr.next = ptr.next.next
    return head
