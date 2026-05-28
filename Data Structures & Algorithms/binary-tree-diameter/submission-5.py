# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # idea: for each node we as we go down, we see its right + left distance, and we just 
        # do the largest of that
        count = 0

        def dfs(root):
            nonlocal count
            if not root:
                return 0
            
            l = dfs(root.left)
            r = dfs(root.right)

            count = max(count, l + r)

            return 1 + max(l, r)
        
        dfs(root)
        return count






