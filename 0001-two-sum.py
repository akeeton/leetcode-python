class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, m in enumerate(nums):
            for j, n in enumerate(nums):
                if i != j and m + n == target:
                    return [i, j]

if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
