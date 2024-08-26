"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                for child in node.children:
                    q.append(child)