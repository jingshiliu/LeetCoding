class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head):
    """
    separate odd list and even list
    but without creating dummy pointers
    """
    if not head: return None
    odd, even, even_head = head, head.next, head.next
    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next

        even = even.next

    odd.next = even_head

    return head


def oddEvenList2(head):
    """
    separate odd list and even list
    """
    if not head: return None
    ptr, even_head = head, ListNode()
    even_tail = even_head
    while ptr and ptr.next:
        even_node = ptr.next

        ptr.next = even_node.next

        even_tail.next = even_node
        even_tail = even_tail.next
        even_tail.next = None

        if not ptr.next: break
        ptr = ptr.next

    ptr.next = even_head.next

    return head


def oddEvenList3(head):
    """
    iterate through list to get tail
    move even node to tail directly

    CONS: iterate list twice
    """
    if not head: return None
    ptr, tail, old_tail = head, head, None

    while tail.next:
        tail = tail.next

    old_tail = tail
    first_even = head.next
    while ptr and ptr != old_tail and ptr != first_even:
        even_node = ptr.next

        # move even_node to the end of list, and update tail pointer
        tail.next = even_node
        tail = tail.next

        # current pointer, skip the even node
        ptr.next = even_node.next
        even_node.next = None

        ptr = ptr.next

    return head