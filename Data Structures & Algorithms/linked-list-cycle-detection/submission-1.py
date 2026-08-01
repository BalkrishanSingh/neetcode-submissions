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
            turtle = turtle.next
            if (hare := hare.next) is not None:
                hare = hare.next
            else:
                return False
            if turtle == hare:
                return True
        return False