# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # go all the way right, if can't find right make a left add that then go right again
        res = []

        def dfs(root, depth):
            nonlocal res

            if not root:
                return
            
            if len(res) == depth:
                res.append(root.val)
            
            dfs(root.right, 1 + depth)
            dfs(root.left, 1 + depth)
            

        dfs(root, 0)

        return res