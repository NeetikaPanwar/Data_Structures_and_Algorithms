# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_size = 0
        node = head
        if n < 1:
            return None
        if head is None:
            return None
        while node:
            list_size += 1
            node = node.next

        if list_size >= n:
            pos = list_size - n

            if pos == 0:
                return head.next

            i = 0
            node = head
            while i < (pos - 1):
                node = node.next
                i += 1

            temp = node.next.next
            node.next = temp

        return head