# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if len(lists) > i + 1 else None

                mergedLists.append(self.mergeLists(l1, l2))

            lists = mergedLists

        return lists[0]

    def mergeLists(self, l1, l2):
        if not l2:
            return l1

        res = ListNode()
        pointer = res

        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = l1
                pointer = pointer.next
                l1 = l1.next
            else:
                pointer.next = l2
                pointer = pointer.next
                l2 = l2.next

        pointer.next = l1 if l1 else l2

        return res.next
