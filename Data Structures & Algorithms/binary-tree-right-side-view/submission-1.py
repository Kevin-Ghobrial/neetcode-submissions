# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        q = deque()
        q.append(root)

        def bfs(q):
            if not q:
                return
            
            subset = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    subset.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if subset:
                res.append(subset[len(subset) - 1])
            
            bfs(q)

        bfs(q)
        return res
            