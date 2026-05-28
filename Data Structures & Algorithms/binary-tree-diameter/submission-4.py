# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        longest = 0

        def dfs(root):
            nonlocal longest

            if root == None:
                return 0
            
            longest = max(longest, dfs(root.left) + dfs(root.right))
            return 1 + max(dfs(root.left), dfs(root.right))

        dfs(root)
        return longest
            

        
        