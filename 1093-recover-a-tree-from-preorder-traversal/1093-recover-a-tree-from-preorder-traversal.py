# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levels=[]
        depth=0
        seen=set()
        for i in range(len(traversal)):
            if i in seen:
                continue
            if traversal[i]=="-":
                depth+=1
            else:
                j=i
                value=""
                while j<len(traversal) and traversal[j]!="-":
                    value+=traversal[j]
                    seen.add(j)
                    j+=1
                node=TreeNode(int(value))

                if depth<len(levels):
                    levels[depth]=node
                else:
                    levels.append(node)

                if depth>0:
                    parent=levels[depth-1]
                    if not parent.left:
                        parent.left=node
                    else:
                        parent.right=node
                    depth=0

        return levels[0]