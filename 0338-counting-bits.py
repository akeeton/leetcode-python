class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        one_bits_counts = [0]

        for n in range(1, num + 1):
            if n % 2 == 0:
                extra = 0
            else:
                extra = 1

            one_bits_counts.append(one_bits_counts[n // 2] + extra)

        return one_bits_counts


def main():
    sol = Solution()

    print(sol.countBits(0))
    print(sol.countBits(2))
    print(sol.countBits(5))


if __name__ == '__main__':
    main()

