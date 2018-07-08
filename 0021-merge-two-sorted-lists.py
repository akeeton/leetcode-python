# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def from_list(vals: list):
        assert(len(vals) > 0)

        node = ListNode(vals[0])

        if len(vals) > 1:
            node.next = ListNode.from_list(vals[1:])

        return node

    def __str__(self):
        s = ""
        node = self
        while node is not None:
            s += "{} -> ".format(node.val)
            node = node.next

        return s[:-4]

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


def main():
    sol = Solution()
    list_a = ListNode.from_list([1, 2, 4])
    list_b = ListNode.from_list([1, 3, 4])

    print(list_a)
    print(list_b)


if __name__ == '__main__':
    main()
