# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # binary search trees have the property
        # to have a lower val on the left and heigher on the right
        # we check and once p and q split from each other, we return that node

        # [5,3,8,1,4,7,9,null,2]
        # p = 3
        # q = 4

        def dfs(root):
            
            if not root:
                return 
            
            if p.val == root.val:
                return root
            if q.val == root.val:
                return root

            if (p.val < root.val) and (q.val > root.val):
                return root
            elif (p.val > root.val) and (q.val < root.val):
                return root
            else:
                if p.val < root.val and q.val < root.val:
                    return dfs(root.left)
                else:
                    return dfs(root.right)
            
        return dfs(root)
        
            



