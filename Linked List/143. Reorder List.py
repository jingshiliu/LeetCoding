def reorderList(self, head) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    fast, slow = head, head

    while fast.next and fast.next.next:
        fast, slow = fast.next.next, slow.next

    if fast.next:
        fast = fast.next
    elif fast == slow:
        return

    while slow.next != fast:
        temp = slow.next
        slow.next = temp.next
        temp.next = fast.next
        fast.next = temp
    slow.next = None

    headPointer = head
    while fast:
        temp = fast
        fast = fast.next
        temp.next = headPointer.next
        headPointer.next = temp
        headPointer = temp.next