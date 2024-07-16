# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start_path=[]
        dest_path=[]

        self.find_path(root,startValue,start_path)
        self.find_path(root,destValue,dest_path)

        directions=[]
        common_path_length=0

        while (common_path_length<len(start_path) and common_path_length<len(dest_path) and start_path[common_path_length]==dest_path[common_path_length]):

            common_path_length+=1

        directions.extend('U'*(len(start_path)-common_path_length))

        directions.extend(dest_path[common_path_length:])

        return "".join(directions)

    def find_path(self,node,target,path):
        if node is None:
            return False
        
        if node.val==target:
            return True

        path.append('L')
        if self.find_path(node.left,target,path):
            return True
        path.pop()

        path.append('R')
        if self.find_path(node.right,target,path):
            return True
        path.pop()

        return False