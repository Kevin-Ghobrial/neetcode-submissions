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
        
        if not head:
            return None
            
        oldToNew = {}
        cur = head

        # first pass to put all nodes in map
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head

        # second pass to make the list
        while cur:
            newNode = oldToNew[cur]
            newNode.next = oldToNew.get(cur.next)
            newNode.random = oldToNew.get(cur.random)
            cur = cur.next
        
        return oldToNew[head]
            