class Sums:
    def __init__(self, left, all, right):
        self.left = left
        self.all = all
        self.right = right

    def __str__(self):
        return str((self.left, self.all, self.right))

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
            return Sums(nums[index_left], nums[index_left], nums[index_left])

        # TODO: remove
        nums_effective = nums[index_left:index_right + 1]

        index_mid = index_left + length // 2

        sums_left = Solution.max_sub_array_rec(nums, index_left, index_mid - 1)
        sums_right = Solution.max_sub_array_rec(nums, index_mid + 1, index_right)

        sum_max_left = sums_left.max()
        sum_max_right = sums_right.max()
        sum_max_all = max(sums_left.all, sums_left.right) + nums[index_mid] + max(sums_right.left, sums_right.all)

        return Sums(sum_max_left, sum_max_all, sum_max_right)

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Condense +/- neighbors so the list looks like [+, -, +] / [+, -, +, -, +] / [+, -, +, -, + -, +],
        # [+, -, +, -, +, -, + -, +].
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
    print(sol.maxSubArray([8, -19, 5, -4, 20]))
    # print(sol.maxSubArray([-1, -1, 1, 1, 1, 1, -1, -1]))
    # print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(sol.maxSubArray([-1]))


if __name__ == '__main__':
    main()
