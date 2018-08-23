"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums_seen = set()
        for num in nums:
            nums_seen.add(num)

        nums_not_seen = []
        for n in range(1, len(nums) + 1):
            if n not in nums_seen:
                nums_not_seen.append(n)

        return nums_not_seen


def main():
    sol = Solution()

    print(sol.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))


if __name__ == '__main__':
    main()
