# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.hashset=set([0])
        root.val=0
        self.recover(root)

    def recover(self,root):
        if root is None:
            return 

        if root.left:
            root.left.val=2*root.val+1
            self.hashset.add(root.left.val)

        if root.right:
            root.right.val=2*root.val+2
            self.hashset.add(root.right.val)

        if root.left:
            self.recover(root.left)

        if root.right:
            self.recover(root.right)

    def find(self, target: int) -> bool:
        return target in self.hashset

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)