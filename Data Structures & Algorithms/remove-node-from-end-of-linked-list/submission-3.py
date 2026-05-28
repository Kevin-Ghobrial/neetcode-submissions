# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # fast and slow concept

        dummy = ListNode(0, head)

        # head -> 1 -> 2
        fast = dummy
        slow = dummy
        for _ in range(n):
            fast = fast.next
        
        # 2 -> 3 -> 4
        # head -> 1 -> 2
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next
