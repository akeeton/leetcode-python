class Solution:
    def climbStairs(self, num_steps):
        """
        :type num_steps int
        :rtype: int
        """

        ways_to_climb_two_fewer_steps = 1
        ways_to_climb_one_fewer_step = 2
        ways_to_climb_n_steps = None

        for n in range(3, num_steps + 1):
            ways_to_climb_n_steps = ways_to_climb_two_fewer_steps + ways_to_climb_one_fewer_step

            ways_to_climb_two_fewer_steps = ways_to_climb_one_fewer_step
            ways_to_climb_one_fewer_step = ways_to_climb_n_steps

        if num_steps == 1:
            return 1
        elif num_steps == 2:
            return 2
        else:
            return ways_to_climb_n_steps


def main():
    sol = Solution()
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))
    print(sol.climbStairs(35))


if __name__ == '__main__':
    main()
