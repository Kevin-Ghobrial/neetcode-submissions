# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # idea: do a dfs down both trees and compare 

        isFalse = False
        def dfs(r1, r2):
            nonlocal isFalse
            
            if not r1 and not r2:
                return
            elif not r1 and r2:
                isFalse = True
                return
            elif r1 and not r2:
                isFalse = True
                return
            elif r1.val != r2.val:
                isFalse = True
                return
            
            dfs(r1.left, r2.left)
            dfs(r1.right, r2.right)
        
        dfs(p, q)
        if isFalse:
            return False
        return True