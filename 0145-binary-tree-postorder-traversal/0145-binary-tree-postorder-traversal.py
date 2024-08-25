# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _postorder_traversal_helper(self,root,result):
        if not root:
            return
        
        self._postorder_traversal_helper(root.left,result)
        self._postorder_traversal_helper(root.right,result)

        result.append(root.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        self._postorder_traversal_helper(root,result)
        return result