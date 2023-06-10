class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapPairs(head):
    # a, which is the node before the 2 nodes that are swapping
    # b, first node been swapped
    # c, second node
    if not head or not head.next: return head

    newHead = ListNode(0, head)
    a = newHead
    while a and a.next and a.next.next:
        b = a.next
        c = b.next

        # swap
        b.next = c.next
        c.next = b
        a.next = c

        # update pointer a
        a = b

    return newHead.next
