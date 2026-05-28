# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        h1 = list1
        h2 = list2
        node = ListNode()
        dummy = node

        while h1 and h2:
            if h1.val > h2.val:
                node.next = h2
                h2 = h2.next
            elif h1.val < h2.val:
                node.next = h1
                h1 = h1.next
            else:
                node.next = h1
                h1 = h1.next
                node = node.next
                node.next = h2
                h2 = h2.next
            node = node.next
        
        node.next = h1 or h2
        return dummy.next