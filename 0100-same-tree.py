# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def pre_order_traversal(tree_node):
        """
        :type tree_node: TreeNode
        :rtype: list
        """

        if tree_node is None:
            return [None]

        vals_left = Solution.pre_order_traversal(tree_node.left)
        vals_right = Solution.pre_order_traversal(tree_node.right)

        return [tree_node.val] + vals_left + vals_right

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        return Solution.pre_order_traversal(p) == Solution.pre_order_traversal(q)


def main():
    sol = Solution()

    tree_a = TreeNode(1)
    tree_a.left = TreeNode(2)
    tree_a.right = TreeNode(3)
    print(Solution.pre_order_traversal(tree_a))

    tree_b = TreeNode(1)
    tree_b.left = TreeNode(2)
    print(Solution.pre_order_traversal(tree_b))

    tree_c = TreeNode(1)
    tree_c.right = TreeNode(2)
    print(Solution.pre_order_traversal(tree_c))

    tree_d = TreeNode(1)
    tree_d.left = TreeNode(2)
    tree_d.right = TreeNode(1)
    print(Solution.pre_order_traversal(tree_d))

    tree_e = TreeNode(1)
    tree_e.left = TreeNode(1)
    tree_e.right = TreeNode(2)
    print(Solution.pre_order_traversal(tree_e))

    print(sol.isSameTree(tree_a, tree_a))
    print(sol.isSameTree(tree_b, tree_c))
    print(sol.isSameTree(tree_d, tree_e))


if __name__ == '__main__':
    main()
