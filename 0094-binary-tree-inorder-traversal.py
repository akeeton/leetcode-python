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

    def __repr__(self):
        return "TreeNode val: {}".format(self.val)


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

    @staticmethod
    def inorder_traversal_iterative(root):
        if root is None:
            return []

        traversal = []
        visited = set()
        stack = [root]

        while len(stack) > 0:
            node_top = stack[-1]

            if node_top.left and node_top.left not in visited:
                stack.append(node_top.left)
                continue

            traversal.append(node_top.val)
            visited.add(node_top)
            stack.pop()

            if node_top.right and node_top.right not in visited:
                stack.append(node_top.right)
                continue

        return traversal

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # return Solution.inorder_traversal_recursive(root)
        return Solution.inorder_traversal_iterative(root)


def main():
    sol = Solution()

    tree_a = TreeNode(1)
    tree_a.left = None
    tree_a.right = TreeNode(2)
    tree_a.right.left = TreeNode(3)
    tree_a.right.right = None

    print(sol.inorderTraversal(tree_a))

    tree_b = TreeNode(1)

    tree_b.left = TreeNode(2)
    tree_b.right = TreeNode(3)

    tree_b.left.left = TreeNode(4)
    tree_b.left.right = TreeNode(5)

    tree_b.right.left = TreeNode(6)
    tree_b.right.right = TreeNode(7)

    print(sol.inorderTraversal(tree_b))


if __name__ == '__main__':
    main()
