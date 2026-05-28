# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
    
        def same(root, root2):
            
            if not root and not root2:
                return True
            if not root or not root2:
                return False
            if root.val != root2.val:
                return False
            
            return same(root.left, root2.left) and same(root.right, root2.right)

        
        def dfs(root):

            if not root:
                return False

            if root.val == subRoot.val and same(root, subRoot):
                return True
            
            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)

