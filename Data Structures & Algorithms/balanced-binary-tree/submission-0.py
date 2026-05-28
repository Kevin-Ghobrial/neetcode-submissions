# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        valid = True

        def dfs(root):
            nonlocal valid

            left = 0
            right = 0
            if root.left:
                left = dfs(root.left)
            if root.right:
                right = dfs(root.right)

            if abs(left - right) > 1:
                valid = False
        
            return max(left, right) + 1
        
        dfs(root)

        return valid