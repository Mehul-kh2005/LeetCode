"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result=[]

        def traversal(root):
            if not root:
                return []

            result.append(root.val)
            for child in root.children:
                traversal(child)

            return result

        return traversal(root)