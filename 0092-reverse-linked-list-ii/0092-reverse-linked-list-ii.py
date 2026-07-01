# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        new_head = ListNode(0)
        start = new_head

        while left > 1 and head != None:
            new_head.next = head
            new_head = new_head.next
            head = head.next
            left -= 1
            right -= 1

        reverse_head = None
        reverse_tail = head

        while right > 0 and head != None:
            next_node = head.next
            head.next = reverse_head
            reverse_head = head
            head = next_node
            right -= 1

        new_head.next = reverse_head
        if reverse_tail != None:
            reverse_tail.next = head

        return start.next