class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        self.inorder(root, nodes)
        return self.buildBST(nodes, 0, len(nodes)-1)

    def inorder(self, root: TreeNode, nodes):
        if not root:
            return 
        self.inorder(root.left, nodes)
        nodes.append(root)
        self.inorder(root.right, nodes)

    def buildBST(self, nodes, left, right) -> TreeNode:
        if left > right:
            return None
        mid = (left + right)//2
        node = nodes[mid]
        node.left = self.buildBST(nodes, left, mid-1)
        node.right = self.buildBST(nodes, mid+1, right)
        return node