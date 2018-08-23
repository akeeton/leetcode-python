"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        counter = Counter(nums)
        most_common = counter.most_common(k)

        return [n for (n, _) in most_common]


def main():
    sol = Solution()

    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))


if __name__ == '__main__':
    main()
