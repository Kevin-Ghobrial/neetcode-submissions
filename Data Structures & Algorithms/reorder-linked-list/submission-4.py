import copy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        v_map = {}
        cur = head
        n = 0
        while cur:
            v_map[n] = cur
            cur = cur.next
            n += 1

        # [2, 8, 4, 6]
        dummy = res = ListNode(None)
        even = True
        offset = 0
        for i in range(n):
            if even:
                print(v_map[offset].val)
                res.next = v_map[offset]
                even = False
            else:
                print(v_map[n - offset - 1].val)
                offset += 1
                res.next = v_map[n - offset]
                even = True
            res = res.next
        res.next = None
        head = res

        

