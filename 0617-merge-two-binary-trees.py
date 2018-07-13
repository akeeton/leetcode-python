# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        left_str = "" if self.left is None else str(self.left)
        right_str = "" if self.right is None else str(self.right)

        return "{} {} {}".format(left_str, self.val, right_str)


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        tree_merged = None

        if t1 is None and t2 is None:
            tree_merged = None
        elif t1 is not None and t2 is None:
            tree_merged = t1
        elif t1 is None and t2 is not None:
            tree_merged = t2
        else:
            tree_merged = TreeNode(t1.val + t2.val)
            tree_merged.left = self.mergeTrees(t1.left, t2.left)
            tree_merged.right = self.mergeTrees(t1.right, t2.right)

        return tree_merged
