
def getIntersectionNode(headA, headB):
    """
    Time: O(m + n)
    Space: O(max(m, n))
    """
    visited = set()
    ptr = headA
    while ptr:
        visited.add(ptr)
        ptr = ptr.next

    ptr = headB
    while ptr and ptr not in visited:
        ptr = ptr.next

    return ptr if ptr != None else None

