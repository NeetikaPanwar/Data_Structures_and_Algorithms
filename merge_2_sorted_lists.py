# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode()
        result_tail = result

        while list1 and list2:
            if list1.val <= list2.val:
                result_tail.next = list1
                list1 = list1.next
            else:
                result_tail.next = list2
                list2 = list2.next
            result_tail = result_tail.next

        if list1 is not None:
            result_tail.next = list1
        else:
            result_tail.next = list2

        return result.next