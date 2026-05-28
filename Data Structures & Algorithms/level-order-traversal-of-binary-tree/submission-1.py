# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = defaultdict(list) # storing roots

        def dfs(root, depth):
            nonlocal res
            
            if not root:
                return None
            
            res[depth].append(root.val)
            dfs(root.left, 1 + depth)
            dfs(root.right, 1 + depth)
        
        dfs(root, 1)

        finalRes = []
        for i in res.values():
            finalRes.append(i)
        
        return finalRes


        
