from collections import Counter


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """

        counter = Counter(nums)
        for item in counter.items():
            if item[1] == 1:
                return item[0]


def main():
    sol = Solution()
    print(sol.singleNumber([2, 2, 1]))
    print(sol.singleNumber([4, 1, 2, 1, 2]))


if __name__ == '__main__':
    main()
