# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        hare = head
        while hare is not None:
            if (hare := hare.next) is None:
                return False
            hare = hare.next
            turtle = turtle.next
            if turtle == hare:
                return True
        return False