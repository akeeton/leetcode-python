"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2
⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        votes = 0
        for num in nums:
            if votes == 0:
                candidate = num

            if num == candidate:
                votes += 1
            else:
                votes -= 1

        return candidate



def main():
    sol = Solution()

    print(sol.majorityElement([3, 2, 3]))
    print(sol.majorityElement([2, 2, 1, 1, 1, 2, 2]))


if __name__ == '__main__':
    main()
