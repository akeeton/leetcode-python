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
    def is_palindrome(s, left, right):
        """
        :param s: str
        :param left: int
        :param right: int
        :return: bool
        """

        length = right - left
        if length == 0:
            return True

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return True

        palindromes = []
        num_palindromes = 0

        for left in range(len(s)):
            for right in range(left, len(s)):
                if Solution.is_palindrome(s, left, right):
                    num_palindromes += 1
                    palindromes.append(s[left:right + 1])

        print(palindromes)
        return num_palindromes


def main():
    sol = Solution()

    print(sol.countSubstrings("abc"))
    print(sol.countSubstrings("aaa"))
    print(sol.countSubstrings("abcdcba"))


if __name__ == '__main__':
    main()
