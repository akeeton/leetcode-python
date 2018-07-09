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
    def mergeTwoLists(self, head_a, head_b):
        """
        :type head_a: ListNode
        :type head_b: ListNode
        :rtype: ListNode
        """

        node_a = head_a
        node_b = head_b
        head_result = None  # type: ListNode
        node_result = None  # type: ListNode

        while True:
            if node_a is None and node_b is None:
                break
            elif node_a is not None and node_b is None:
                val_min = node_a.val
                node_a = node_a.next
            elif node_a is None and node_b is not None:
                val_min = node_b.val
                node_b = node_b.next
            else:
                if node_a.val <= node_b.val:
                    val_min = node_a.val
                    node_a = node_a.next
                else:
                    val_min = node_b.val
                    node_b = node_b.next

            node_new = ListNode(val_min)
            if head_result is None:
                head_result = node_new
                node_result = head_result
            else:
                node_result.next = node_new
                node_result = node_result.next

            pass

        return head_result


def main():
    sol = Solution()
    list_a = ListNode.from_list([1, 2, 4])
    list_b = ListNode.from_list([1, 3, 4])
    list_ab = sol.mergeTwoLists(list_a, list_b)

    print(list_a)
    print(list_b)
    print(list_ab)


if __name__ == '__main__':
    main()
