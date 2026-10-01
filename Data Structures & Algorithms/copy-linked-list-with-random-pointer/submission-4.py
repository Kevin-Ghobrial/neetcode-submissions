"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h_map = {}
        h_map[None] = None

        cur = head
        while cur:
            h_map[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            h_map[cur].next = h_map[cur.next]
            h_map[cur].random = h_map[cur.random]
            cur = cur.next
        
        return h_map[head]