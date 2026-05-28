# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = l1
        prod = 1
        val1 = 0
        while cur1:
            curSum = cur1.val * prod
            val1 += curSum
            prod = prod * 10
            cur1 = cur1.next
        
        cur2 = l2
        prod = 1
        val2 = 0
        while cur2:
            curSum = cur2.val * prod
            val2 += curSum
            prod = prod * 10
            cur2 = cur2.next
        

        total = val1 + val2
        s_total = list(str(total))

        node = ListNode()
        dummy = node
        for i in range(len(s_total) - 1, -1, -1):
            node.next = ListNode(int(s_total[i]))
            node = node.next
        
        return dummy.next


