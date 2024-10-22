# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node,level):
            level_sum[level]+=node.val
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)

        level_sum=defaultdict(int)
        dfs(root,1)
        return min(level_sum, key=lambda x: (-level_sum[x], x))