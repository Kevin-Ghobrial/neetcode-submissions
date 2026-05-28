# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return 
        
        q = deque()
        q.append(root)

        while q:
            invNode = q.popleft()

            if not invNode:
                continue
            
            if invNode.right and invNode.left:
                temp = invNode.right
                invNode.right = invNode.left
                invNode.left = temp
            elif invNode.left:
                temp = invNode.left
                invNode.left = None
                invNode.right = temp
            elif invNode.right:
                temp = invNode.right
                invNode.right = None
                invNode.left = temp

            if invNode.left and not invNode.right:
                q.append(None)
                q.append(invNode.left)
            
            if invNode.left and invNode.right:
                q.append(invNode.left)
                q.append(invNode.right)
            
            if invNode.right and not invNode.left:
                q.append(invNode.right)
        
        return root
            

