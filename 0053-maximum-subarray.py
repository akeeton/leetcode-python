class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum_max = None
        for index_left in range(len(nums)):
            sum_partial = 0

            for index_right in range(index_left, len(nums)):
                sum_partial += nums[index_right]
                sum_max = sum_partial if sum_max is None else max(sum_max, sum_partial)

        return sum_max


def main():
    sol = Solution()
    # print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(sol.maxSubArray([-1]))


if __name__ == '__main__':
    main()
