class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = 1
        if x < 0:
            sign = -1
            x *= -1

        x_reversed = 0
        while x > 0:
            digit = x % 10

            x_reversed *= 10
            x_reversed += digit

            x //= 10

        x_reversed *= sign

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if INT_MIN <= x_reversed <= INT_MAX:
            return x_reversed
        else:
            return 0


def main():
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(123456))
    print(sol.reverse(-123456))
    print(sol.reverse(1234560))
    print(sol.reverse(-1234560))
    print(sol.reverse(9646324351))
    print(sol.reverse(1534236469))


if __name__ == '__main__':
    main()
