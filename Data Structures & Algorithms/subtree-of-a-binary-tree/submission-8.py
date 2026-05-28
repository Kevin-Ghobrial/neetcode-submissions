# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root):

            if not root:
                return False
            
            if root.val == subRoot.val:
                if same(root, subRoot):
                    return True
            
            return dfs(root.right) or dfs(root.left)


        def same(r1, r2):
            if not r1 and not r2:
                return True
            elif not r1 and r2 or not r2 and r1:
                return False
            elif r1.val != r2.val:
                return False
            
            return same(r1.left, r2.left) and same(r1.right, r2.right)
        
        return dfs(root)



