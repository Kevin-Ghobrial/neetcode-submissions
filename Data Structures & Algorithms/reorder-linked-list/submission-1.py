# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head.next:
            return
        
        # idea: split in 2
        # slow and fast pointer

        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        prev.next = None
        prev2 = None
        while slow:
            temp = slow.next
            slow.next = prev2
            prev2 = slow
            slow = temp

        first = head
        second = prev2
        while first and second:
            t1 = first.next #storing the next node from first list
            t2 = second.next #storing next node from second list

            first.next = second #adding the first node from second list to first list

            if not t1: #if we finish t1 then we finished both lists
                break
            second.next = t1 # cleaver way connect second node from first list to second list

            #increment both lists pointers
            first = t1 
            second = t2
        
        return 

            

            


            