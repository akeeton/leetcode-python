class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i, m in enumerate(nums):
        #     for j, n in enumerate(nums):
        #         if i != j and m + n == target:
        #             return [i, j]

        # d = {}
        # for i, m in enumerate(nums):
        #     for j, n in enumerate(nums):
        #         if i != j and m + n not in d:
        #             d[m + n] = [i, j]
        # return d[target]

        d = {}
        for i, num in enumerate(nums):
            d[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                j = d[diff]
                if i != j:
                    return [i, j]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
