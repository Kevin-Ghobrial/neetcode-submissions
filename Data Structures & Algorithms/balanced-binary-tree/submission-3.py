# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # idea: dfs, check left rank, check right rank.
        # if they differ by more than 1, then return false

        if not root:
            return True
        
        isFalse = False

        def dfs(root):
            nonlocal isFalse

            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)
            print(l, r)
        
            if r - l > 1 or l - r > 1:
                isFalse = True
            
            return 1 + max(l, r)
        
        dfs(root)
        if isFalse:
            return False
        return True
