from ListNode import ListNode

def pairSum(head) -> int:
    """
    Time: O(n)
    Space: O(1)

    reverse the second half
    """
    slow, fast = head, head
    while fast:
        slow = slow.next
        fast = fast.next.next

    # when fast ptr is at end, slow ptr is at the half
    reversed_second_half_head = ListNode()

    while slow:
        cur = slow
        slow = slow.next

        cur.next = reversed_second_half_head.next
        reversed_second_half_head.next = cur

    ptr, reversed_ptr = head, reversed_second_half_head.next
    res = 0
    while reversed_ptr:
        res = max(res, ptr.val + reversed_ptr.val)
        ptr = ptr.next
        reversed_ptr = reversed_ptr.next

    return res


def pairSum1(head) -> int:
    # Time: O(n)
    # Space: O(n)

    # first node is twin of last node
    # second is twin of second from the end
    # third ...

    fast, slow = head, head
    stack = []
    res = 0
    while slow:
        if fast:
            fast = fast.next.next
            stack.append(slow)
        else:
            res = max(res, slow.val + stack.pop().val)

        slow = slow.next

    return res