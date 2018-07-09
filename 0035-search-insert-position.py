class Solution:
    @staticmethod
    def binary_search(nums, target, index_left, index_right):
        """
        :type nums: List[int]
        :type target: int
        :type index_left: int
        :type index_right: int
        :rtype: int
        """

        length = index_right - index_left + 1
        if length == 1:
            if target <= nums[index_left]:
                return index_left
            else:
                return index_left + 1

        index_mid = index_left + length // 2 - 1
        num_mid = nums[index_mid]

        if target == num_mid:
            return index_mid
        elif target < num_mid:
            return Solution.binary_search(nums, target, index_left, index_mid)
        else:
            return Solution.binary_search(nums, target, index_mid + 1, index_right)

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return Solution.binary_search(nums, target, 0, len(nums) - 1)


def main():
    sol = Solution()
    print(sol.searchInsert([1, 3], 4))
    print(sol.searchInsert([1, 3], 0))
    print(sol.searchInsert([0, 1, 2, 3, 4], 4))
    print(sol.searchInsert([1, 3, 5, 6], 5))
    print(sol.searchInsert([1, 3, 5, 6], 2))
    print(sol.searchInsert([1, 3, 5, 6], 7))
    print(sol.searchInsert([1, 3, 5, 6], 0))


if __name__ == '__main__':
    main()
