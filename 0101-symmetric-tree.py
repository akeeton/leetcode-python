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
    @staticmethod
    def are_trees_mirrors(tree_a, tree_b):
        """
        :type tree_a: TreeNode
        :type tree_b: TreeNode
        :rtype: bool
        """

        if tree_a is None and tree_b is None:
            return True

        if tree_a is None or tree_b is None:
            return False

        return tree_a.val == tree_b.val and Solution.are_trees_mirrors(tree_a.right, tree_b.left) and Solution.are_trees_mirrors(tree_a.left, tree_b.right)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return Solution.are_trees_mirrors(root, root)


def main():
    sol = Solution()

    tree_a = TreeNode(1)
    tree_a.left = TreeNode(2)
    tree_a.left.left = TreeNode(3)
    tree_a.left.right = TreeNode(4)
    tree_a.right = TreeNode(2)
    tree_a.right.left = TreeNode(4)
    tree_a.right.right = TreeNode(3)

    print(sol.isSymmetric(tree_a))


if __name__ == '__main__':
    main()
