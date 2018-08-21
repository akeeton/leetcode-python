"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def inorder_traversal_recursive(node):
        """
        :param node: TreeNode
        :return: List[int]
        """

        if node is None:
            return []

        val_left = Solution.inorder_traversal_recursive(node.left)
        val_right = Solution.inorder_traversal_recursive(node.right)

        return val_left + [node.val] + val_right

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        return Solution.inorder_traversal_recursive(root)


def main():
    sol = Solution()

    tree_a = TreeNode(1)
    tree_a.left = None
    tree_a.right = TreeNode(2)
    tree_a.right.left = TreeNode(3)
    tree_a.right.right = None

    print(sol.inorderTraversal(tree_a))


if __name__ == '__main__':
    main()
