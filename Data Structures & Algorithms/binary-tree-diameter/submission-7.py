# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        curMax = float("-inf")

        def dfs(cur):
            nonlocal curMax

            if not cur:
                return 0
            
            left = dfs(cur.left)
            right = dfs(cur.right)

            curMax = max(left + right, curMax)
            return max(left, right) + 1
        
        dfs(root)
        return curMax

