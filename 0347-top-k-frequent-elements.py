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
        buckets = [[] for _ in range(len(nums) + 1)]

        for item in counter.items():
            count = item[1]
            num = item[0]

            buckets[count].append(num)

        result = []
        for nums_with_freq in reversed(buckets):
            if not nums_with_freq:
                continue

            if k == 0:
                break

            n = len(nums_with_freq)
            result += nums_with_freq[0:k]
            k -= n

        return result


def main():
    sol = Solution()

    # print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    # print(sol.topKFrequent(["a", "a", "a", "b", "b", "c"], 2))
    print(sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))  # -1, 2


if __name__ == '__main__':
    main()
