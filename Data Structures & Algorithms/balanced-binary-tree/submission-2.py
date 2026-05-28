# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # idea: check max depth of each side recursivly and return false if diff is greater than 1
        
        isBalanced = True

        def dfs(root):
            nonlocal isBalanced 
            
            if root == None:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            if abs(l - r) > 1:
                isBalanced = False
                return 0
            
            return 1 + max(l, r)

        dfs(root)
        return isBalanced
            
