# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        mid, high, node = head, head, head
        mid_prev = None
        while high and high.next:
            mid_prev = mid
            mid = mid.next
            high = high.next.next

        return mid_prev, mid

    def reverse(self, head):
        prev = None
        node = head

        while node:
            backup = node.next
            node.next = prev
            prev = node
            node = backup

        return prev

    def merge_lists(self, head1, head2):
        result = ListNode()
        tail = result
        i = 0

        while head1 and head2:
            if i % 2 == 0:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            i += 1

            tail = tail.next

        if head1:
            tail.next = head1
        else:
            tail.next = head2
        return result.next

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        if head.next is None:
            return head

        mid_prev, mid = self.find_middle(head)
        mid_prev.next = None

        head2 = self.reverse(mid)

        result = self.merge_lists(head, head2)

        return result

