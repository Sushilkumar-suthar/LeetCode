# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(-float('inf'))
        current_p = result
        while head!=None:
            if head.val>current_p.val:
                current_p.next = ListNode(head.val)
                current_p = current_p.next
            head = head.next
        return result.next