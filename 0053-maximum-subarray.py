class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = None
        max_sum_prev = None
        for index_end, num_at_end in enumerate(nums):
            if index_end == 0:
                max_sum = max_sum_prev = num_at_end
            else:
                max_sum_prev = max(num_at_end, num_at_end + max_sum_prev)
                max_sum = max(max_sum, max_sum_prev)

        return max_sum


def main():
    sol = Solution()
    print(sol.maxSubArray([8, -19, 5, -4, 20]))
    print(sol.maxSubArray([-1, -1, 1, 1, 1, 1, -1, -1]))
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(sol.maxSubArray([-1]))


if __name__ == '__main__':
    main()
