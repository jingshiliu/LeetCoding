class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(head):
    def sort_list(head_node):
        if not (head_node and head_node.next):
            return head_node

        mid = get_mid(head_node)
        right = sort_list(mid.next)
        mid.next = None
        left = sort_list(head_node)

        return merge(left, right)

    def merge(left, right):
        new_head = ListNode()
        ptr = new_head

        while left and right:
            if left.val < right.val:
                ptr.next = left
                left = left.next
            else:
                ptr.next = right
                right = right.next
            ptr = ptr.next

        if left:
            ptr.next = left
        elif right:
            ptr.next = right
        return new_head.next

    def get_mid(head_node):
        mid = None
        while head_node and head_node.next:
            mid = mid.next if mid else head_node
            head_node = head_node.next.next
        return mid

    return sort_list(head)


def sort_list_node_arr(head ):
    if not head: return
    arr = []
    ptr = head
    while ptr:
        arr.append(ptr)
        ptr = ptr.next

    arr.sort(key=lambda x: x.val)

    for i in range(len(arr) - 1):
        arr[i].next = arr[i + 1]

    arr[-1].next = None
    return arr[0]


