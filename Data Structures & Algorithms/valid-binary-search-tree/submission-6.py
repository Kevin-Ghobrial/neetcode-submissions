# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        isBST = True
        def dfs(root, leftMax, rightMin):
            nonlocal isBST

            if not root:
                return

            if root.val >= leftMax or root.val <= rightMin:
                isBST = False

            dfs(root.left, root.val, rightMin)
            dfs(root.right, leftMax, root.val)

        

        dfs(root, float('inf'), float('-inf'))
        return isBST
