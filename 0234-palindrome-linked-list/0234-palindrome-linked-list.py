# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = None
        start = head
        while start!=None:
            t = ListNode(start.val)
            t.next = reverse
            reverse = t
            start = start.next
        
        while reverse != None and head != None:
            if reverse.val != head.val:return False
            reverse = reverse.next
            head = head.next
        return True