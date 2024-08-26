# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        
        q=[root,None]
        b=[]
        result=[]

        while q:
            node=q.pop(0)
            if not node:
                result.append(b)
                b=[]
                if not q:
                    return result
                q.append(None)
            
            else:
                b.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)