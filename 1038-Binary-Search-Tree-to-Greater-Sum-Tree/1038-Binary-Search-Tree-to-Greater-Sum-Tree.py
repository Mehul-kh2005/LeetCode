# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        node_sum = 0
        st = []
        node = root
        while st or node is not None:
            while node is not None:
                st.append(node)
                node = node.right
            # Store the top value of stack in node and pop it.
            node = st.pop()
            # Update value of node.
            node_sum += node.val
            node.val = node_sum
            # Move to the left child of node.
            node = node.left

        return root