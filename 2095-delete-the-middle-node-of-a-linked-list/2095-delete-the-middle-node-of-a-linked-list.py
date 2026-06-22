# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start= head
        half_p = head
        half_prev = None
        does_move = False
        while head != None:
            if does_move: 
                half_prev = half_p
                half_p = half_p.next
                does_move=False
            else:
                does_move=True
            head = head.next
        if half_p!=None:
            if half_prev != None:
                half_prev.next = half_p.next
            else:start = half_prev
        return start