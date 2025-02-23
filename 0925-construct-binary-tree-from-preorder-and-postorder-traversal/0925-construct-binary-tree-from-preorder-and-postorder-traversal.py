# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre_index=0
        self.post_index=0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.constructTree(preorder,postorder)
    
    def constructTree(self,preorder,postorder):
        root=TreeNode(preorder[self.pre_index])
        self.pre_index+=1

        if root.val!=postorder[self.post_index]:
            root.left=self.constructTree(preorder,postorder)
        
        if root.val!=postorder[self.post_index]:
            root.right=self.constructTree(preorder,postorder)

        self.post_index+=1
        return root