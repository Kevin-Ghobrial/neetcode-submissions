# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        count = 0
        def dfs(root, maxNode):

            if not root:
                return
            
            nonlocal count

            if root.val >= maxNode:
                count += 1
                maxNode = root.val
            
            dfs(root.left, maxNode)
            dfs(root.right, maxNode)
        

        dfs(root, root.val)
        return count

            