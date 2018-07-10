class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 2) + self.climbStairs(n - 1)


def main():
    sol = Solution()
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))


if __name__ == '__main__':
    main()
