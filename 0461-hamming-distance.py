class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        hamming_distance = 0
        for i in range(32):
            mask = 1 << i
            bit_x = mask & x
            bit_y = mask & y

            if bit_x != bit_y:
                hamming_distance += 1

        return hamming_distance


def main():
    print(Solution().hammingDistance(1, 4))


if __name__ == '__main__':
    main()
