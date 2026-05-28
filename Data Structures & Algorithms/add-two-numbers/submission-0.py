# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        list1 = []
        list2 = []

        cur1 = l1
        cur2 = l2
        while cur1:
            list1.append(cur1.val)
            cur1 = cur1.next
        while cur2:
            list2.append(cur2.val)
            cur2 = cur2.next
        
        left = (1 * (10 ** len(list1))) // 10
        right = (1 * (10 ** len(list2))) // 10

        lval = 0
        for i in range(len(list1) - 1, -1, -1):
            lval += (list1[i] * left)
            left = left // 10
        
        rval = 0
        for j in range(len(list2) - 1, -1, -1):
            rval += (list2[j] * right)
            right = right // 10

        final_val = lval + rval
        
        final_val = list(str(final_val))
        print(final_val)

        node = ListNode()
        dummy = node

        for i in range(len(final_val) - 1, -1, -1):
            newNode = ListNode(int(final_val[i]))
            node.next = newNode
            node = node.next
        
        return dummy.next
        





        

        