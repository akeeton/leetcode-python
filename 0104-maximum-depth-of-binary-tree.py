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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def main():
    sol = Solution()
    tree_a = TreeNode(3)
    tree_a.left = TreeNode(9)
    tree_a.right = TreeNode(20)
    tree_a.right.left = TreeNode(15)
    tree_a.right.right = TreeNode(7)

    print(tree_a)
    print(sol.maxDepth(tree_a))


if __name__ == '__main__':
    main()
