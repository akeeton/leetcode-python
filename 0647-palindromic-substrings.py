"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of
same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
"""


class Solution:
    @staticmethod
    def is_palindrome(s, left_bound, right_bound):
        """
        :param s: str
        :param left_bound: int
        :param right_bound: int
        :return: bool
        """

        length = right_bound - left_bound + 1
        assert(length >= 1)

        if length % 2 == 0:
            # length is even so treat the middle two characters as a single middle character

            middle_right = length // 2
            middle_left = middle_right - 1

            if s[middle_left] != s[middle_right]:
                return False

            left = middle_left - 1
            right = middle_right + 1
        else:
            # length is odd so start at the middle character

            middle = length // 2
            left = middle - 1
            right = middle + 1

        while left >= left_bound and right <= right_bound:
            if s[left] != s[right]:
                return False

            left -= 1
            right += 1

        return True

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0 or len(s) == 1:
            return True

        palindromes = []
        num_palindromes = 0

        for left_bound in range(len(s)):
            for right_bound in range(len(s) - 1, left_bound - 1, -1):
                if Solution.is_palindrome(s, left_bound, right_bound):
                    num_palindromes += 1
                    palindromes.append(s[left_bound:right_bound + 1])

        print(palindromes)
        return num_palindromes


def main():
    sol = Solution()

    # print(sol.countSubstrings("abc"))
    # print(sol.countSubstrings("aaa"))
    print(sol.countSubstrings("abcdcba"))


if __name__ == '__main__':
    main()
