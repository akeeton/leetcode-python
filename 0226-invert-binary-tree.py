from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        # left_str = "" if self.left is None else str(self.left)
        # right_str = "" if self.right is None else str(self.right)
        #
        # return "{} {} {}".format(left_str, self.val, right_str)

        s = ""
        queue = deque()
        queue.appendleft(self)

        while len(queue) > 0:
            node = queue.pop()
            s += "{} ".format(node.val)

            if node.left is not None:
                queue.appendleft(node.left)

            if node.right is not None:
                queue.appendleft(node.right)

        return s[:-1]


class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None

        queue = deque()
        queue.appendleft(root)

        while len(queue) > 0:
            node = queue.pop()

            child_temp = node.left
            node.left = node.right
            node.right = child_temp

            if node.left is not None:
                queue.appendleft(node.left)

            if node.right is not None:
                queue.appendleft(node.right)

        return root


def main():
    sol = Solution()

    tree_a = TreeNode(4)
    tree_a.left = TreeNode(2)
    tree_a.left.left = TreeNode(1)
    tree_a.left.right = TreeNode(3)
    tree_a.right = TreeNode(7)
    tree_a.right.left = TreeNode(6)
    tree_a.right.right = TreeNode(9)

    print(tree_a)
    print(sol.invertTree(tree_a))


if __name__ == '__main__':
    main()
