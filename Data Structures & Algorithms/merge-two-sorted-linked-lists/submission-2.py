# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        node = ListNode()
        dummy = node

        while cur1 and cur2:

            if cur1.val < cur2.val:
                node.next = cur1
                cur1 = cur1.next
            else:
                node.next = cur2
                cur2 = cur2.next
            node = node.next
        
        # just append the rest of the list to it, smart
        node.next = cur1 or cur2
    
        return dummy.next



