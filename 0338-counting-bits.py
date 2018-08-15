class Solution:
    @staticmethod
    def binary_ones(n):
        """
        :param n: int
        :return: int
        """

        num_ones = 0
        while n > 0:
            num_ones += 0x1 & n
            n >>= 1

        return num_ones

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        ones_for_n = []
        for n in range(num + 1):
            ones_for_n.append(Solution.binary_ones(n))

        return ones_for_n


def main():
    sol = Solution()

    print(sol.countBits(2))
    print(sol.countBits(5))


if __name__ == '__main__':
    main()

