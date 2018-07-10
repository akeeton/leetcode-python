class Solution:
    @staticmethod
    def max_sub_arrays_ending_with_index(nums):
        max_sums = []

        for index_end, num_at_end in enumerate(nums):
            if index_end == 0:
                max_sums.append(num_at_end)
            else:
                max_sums.append(max(num_at_end, num_at_end + max_sums[index_end - 1]))

        return max_sums

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return max(Solution.max_sub_arrays_ending_with_index(nums))


def main():
    sol = Solution()
    print(sol.maxSubArray([8, -19, 5, -4, 20]))
    print(sol.maxSubArray([-1, -1, 1, 1, 1, 1, -1, -1]))
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(sol.maxSubArray([-1]))


if __name__ == '__main__':
    main()
