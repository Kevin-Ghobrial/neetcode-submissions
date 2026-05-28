# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # idea, store a max value and then add to count if node is less that it and turn that into the max
        # run a dfs

        def dfs(root, maxVal):

            if not root:
                return 0

            if root.val >= maxVal:
                res = 1
            else:
                res = 0
            
            maxVal = max(maxVal, root.val) 

            # goes down own path so maxVal will be consistent
            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)
            return res
        
        return dfs(root, root.val)
            
