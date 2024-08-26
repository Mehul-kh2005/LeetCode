"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result=[]

        def traversal(root):
            if not root:
                return
            for child in root.children:
                traversal(child)

            result.append(root.val)

        traversal(root)
        return result