# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        q = deque()
        q.append(root)
        count = 0

        # idea, for each level just add to count
        # do a bfs from root?
        # really simple actually
        # just append the entire level to the queue
        # then add to the level while we still have values in the queue

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            count += 1
    
        return count
      
        