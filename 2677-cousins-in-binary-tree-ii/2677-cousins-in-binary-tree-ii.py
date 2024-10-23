class Solution:
    def __init__(self):
        self.level_sums = [0] * 100000

    def replaceValueInTree(self, root):
        self._calculate_level_sum(root, 0)
        self.replace_value_in_tree_internal(root, 0, 0)
        return root

    def _calculate_level_sum(self, node, level):
        if node is None:
            return
        self.level_sums[level] += node.val
        self._calculate_level_sum(node.left, level + 1)
        self._calculate_level_sum(node.right, level + 1)

    def replace_value_in_tree_internal(self, node, sibling_sum, level):
        if node is None:
            return
        left_child_val = 0 if node.left is None else node.left.val
        right_child_val = 0 if node.right is None else node.right.val

        if level == 0 or level == 1:
            node.val = 0
        else:
            node.val = self.level_sums[level] - node.val - sibling_sum
        self.replace_value_in_tree_internal(
            node.left, right_child_val, level + 1
        )
        self.replace_value_in_tree_internal(
            node.right, left_child_val, level + 1
        )