class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ""
        n = self

        while n is not None:
            s += " -> {}".format(n.val)
            n = n.next

        s = s[3:]
        return s


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        node1 = l1
        node2 = l2
        is_first_loop = True
        carry = 0

        result = None  # type: ListNode
        result_highest_node = None  # type: ListNode

        while node1 is not None or node2 is not None or carry == 1:
            digit1 = 0 if node1 is None else node1.val
            digit2 = 0 if node2 is None else node2.val

            digit_sum = digit1 + digit2 + carry
            if digit_sum >= 10:
                result_digit = digit_sum % 10
                carry = 1
            else:
                result_digit = digit_sum
                carry = 0

            if is_first_loop:
                result_highest_node = ListNode(result_digit)
                result = result_highest_node
                is_first_loop = False
            else:
                result_highest_node.next = ListNode(result_digit)
                result_highest_node = result_highest_node.next

            node1 = node1.next if node1 is not None else None
            node2 = node2.next if node2 is not None else None

        return result


def main():
    solution = Solution()

    l1 = ListNode(5)
    # l1.next = ListNode(4)
    # l1.next.next = ListNode(3)
    print(l1)

    l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)
    print(l2)

    result = solution.addTwoNumbers(l1, l2)
    print(result)


if __name__ == '__main__':
    main()
