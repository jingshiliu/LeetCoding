# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curHead, curTail = head, head
        nextHead = None
        i = 0
        resHead = None
        isFirstSection = True
        while i < k and curTail:
            self.printList(head)
            curTail = curTail.next
            i += 1
            if i == k - 1:
                # Res head is first section's tail
                if isFirstSection:
                    resHead = curTail
                    isFirstSection = False
                # reverse section
                nextHead = curTail.next
                while curHead.next != nextHead:
                    cur = curHead.next
                    curHead.next = cur.next
                    cur.next = curHead

                curHead, curTail = nextHead, nextHead
                i = 0

        return resHead

    def printList(self, head):
        while head:
            print(head.val)
            head = head.next
