# class Solution:
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         sum_max = None
#         for index_left in range(len(nums)):
#             sum_partial = 0
#
#             for index_right in range(index_left, len(nums)):
#                 sum_partial += nums[index_right]
#                 sum_max = sum_partial if sum_max is None else max(sum_max, sum_partial)
#
#         return sum_max


class Sums:
    def __init__(self, left, all, right):
        self.left = left
        self.all = all
        self.right = right

    def max(self):
        return max(self.left, self.all, self.right)


class Solution:
    @staticmethod
    def max_sub_array_rec(nums, index_left, index_right):
        """
        :rtype: Sums
        """

        length = index_right - index_left + 1
        if length == 1:
            return Sums(nums[index_left], 0, 0)

        # TODO: remove
        nums_effective = nums[index_left:index_right + 1]

        index_mid = index_left + length // 2

        sums_left = Solution.max_sub_array_rec(nums, index_left, index_mid - 1)
        sums_right = Solution.max_sub_array_rec(nums, index_mid + 1, index_right)

        sum_max_left = sums_left.max()
        sum_max_right = sums_right.max()
        sum_max_all = sums_left.all + nums[index_mid] + sums_right.all

        return Sums(sum_max_left, sum_max_all, sum_max_right)
        # if num_mid > 0:
        #     sum_max_left += num_mid
        #     sum_max_right += num_mid

        # sum_max = max(sum_all, sum_max_left, sum_max_right)
        # return sum_max

        # if sum_max_left > 0 and sum_max_right > 0:
        #     return sum_max_left + sum_max_right
        # elif sum_max_left <= 0 and sum_max_right <= 0:
        #     return max(sum_max_left, sum_max_right)
        # elif sum_max_left <= 0 < sum_max_right:
        #     return sum_max_right
        # elif sum_max_left > 0 >= sum_max_right:
        #     return sum_max_left

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Condense +/- neighbors so the list looks like [+, -, +] / [+, -, +, -, +] / [+, -, +, -, + -, +].
        nums_condensed = []
        sum_running = None
        for num in nums:
            if sum_running is None:
                sum_running = num
            elif sum_running >= 0 > num:
                nums_condensed.append(sum_running)
                sum_running = num
            elif sum_running < 0 <= num:
                nums_condensed.append(sum_running)
                sum_running = num
            else:
                sum_running += num

        if sum_running is not None:
            nums_condensed.append(sum_running)

        if len(nums_condensed) == 1:
            return nums_condensed[0]

        if nums_condensed[0] < 0:
            nums_condensed.pop(0)

        if nums_condensed[-1] < 0:
            nums_condensed.pop()

        print(nums_condensed)
        return Solution.max_sub_array_rec(nums_condensed, 0, len(nums_condensed) - 1).max()


def main():
    sol = Solution()
    # print(sol.maxSubArray([-1, -1, 1, 1, 1, 1, -1, -1]))
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(sol.maxSubArray([-1]))


if __name__ == '__main__':
    main()
