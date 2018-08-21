"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the
non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    @staticmethod
    def bubble_sort_zeroes(nums):
        is_sorted = False

        while not is_sorted:
            is_sorted = True

            for left in range(len(nums) - 1):
                right = left + 1

                if nums[left] == 0 and nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    is_sorted = False

    @staticmethod
    def insertion_sort_zeroes(nums):
        for index_unsorted, num in enumerate(nums):
            if index_unsorted == 0 or num == 0:
                continue

            for index_search_for_zero in range(index_unsorted):
                if nums[index_search_for_zero] == 0:
                    nums[index_search_for_zero] = num
                    nums[index_unsorted] = 0

                    break


    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # Solution.bubble_sort_zeroes(nums)
        Solution.insertion_sort_zeroes(nums)


def main():
    sol = Solution()

    nums_a = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums_a)
    print(nums_a)


if __name__ == '__main__':
    main()
