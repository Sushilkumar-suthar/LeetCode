# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        start= head
        half_p = head
        half_prev = None
        
        while head and head.next:
            half_prev = half_p
            half_p = half_p.next
            head = head.next.next

        half_prev.next = half_p.next
        return start