# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node,level):
            level_sum[level]+=node.val
            if node.left:
                dfs(node.left,level+1)
            if node.right:
                dfs(node.right,level+1)

        level_sum=defaultdict(int)
        dfs(root,1)

        if len(level_sum)<k:
            return -1
        
        return sorted(level_sum.values())[-k]        