# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete=set(to_delete)
        forest=[]

        root=self.delNodesHelper(root,to_delete,forest)
        if root:
            forest.append(root)

        return forest

    def delNodesHelper(self,node,to_delete,forest):
        if not node:
            return None
        
        node.left=self.delNodesHelper(node.left,to_delete,forest)
        node.right=self.delNodesHelper(node.right,to_delete,forest)

        if node.val in to_delete:
            if node.left:
                forest.append(node.left)

            if node.right:
                forest.append(node.right)

            return None

        return node