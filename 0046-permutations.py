"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    @staticmethod
    def permute_using_set(nums):
        """
        :type nums: Set[int]
        :rtype: List[List[int]]
        """

        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [[next(iter(nums))]]

        nums_copy = nums.copy()
        permutations = []

        for num in nums:
            nums_copy.remove(num)

            partial_permutations = Solution.permute_using_set(nums_copy)

            for partial_permutation in partial_permutations:
                permutations.append([num] + partial_permutation)

            nums_copy.add(num)

        return permutations

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        return Solution.permute_using_set(set(nums))


def main():
    sol = Solution()

    print(sol.permute([1, 2, 3]))


if __name__ == '__main__':
    main()