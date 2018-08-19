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
    def is_palindrome(s):
        """
        :param s: str
        :return: bool
        """

        if len(s) == 0 or len(s) == 1:
            return True

        left = 0
        right = len(s) - 1

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

        palindromes = []

        for left in range(len(s)):
            for right in range(left, len(s)):
                substring = s[left:right + 1]

                if Solution.is_palindrome(substring):
                    palindromes.append(substring)

        print(palindromes)
        return len(palindromes)


def main():
    sol = Solution()

    print(sol.countSubstrings("abc"))
    print(sol.countSubstrings("aaa"))
    print(sol.countSubstrings("abcdcba"))


if __name__ == '__main__':
    main()
