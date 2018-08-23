"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up: Could you solve it with constant space complexity? (The output array does not count as extra space for the
purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        products_to_the_left = [None] * len(nums)
        products_to_the_right = [None] * len(nums)

        for loop in range(len(nums)):
            index_left = loop
            index_right = len(nums) - 1 - loop

            if loop == 0:
                products_to_the_left[index_left] = 1
                products_to_the_right[index_right] = 1
                continue

            products_to_the_left[index_left] = products_to_the_left[index_left - 1] * nums[index_left - 1]
            products_to_the_right[index_right] = products_to_the_right[index_right + 1] * nums[index_right + 1]

        products = []

        for i in range(len(nums)):
            products.append(products_to_the_left[i] * products_to_the_right[i])

        return products


def main():
    sol = Solution()

    print(sol.productExceptSelf([1, 2, 3, 4]))


if __name__ == '__main__':
    main()
