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
    def do_stuff(s, left_bound, right_bound, palindromes):
        """
        :param s: str
        :param left_bound: int
        :param right_bound: int
        :param palindromes: List[str]
        :return: int
        """

        num_palindromes = 0

        slice = s[left_bound:right_bound + 1]

        length = right_bound - left_bound + 1
        assert(length >= 1)

        if length % 2 == 0:
            # length is even so treat the middle two characters as a single middle character

            middle_right = left_bound + length // 2
            middle_left = middle_right - 1

            if s[middle_left] != s[middle_right]:
                return 0

            left = middle_left
            right = middle_right
        else:
            # length is odd so start at the middle character

            middle = left_bound + length // 2
            left = middle
            right = middle

        while left >= left_bound and right <= right_bound and right - left + 1 > 1:
            if s[left] == s[right]:
                palindromes.append(s[left:right + 1])
                num_palindromes += 1
            else:
                break

            left -= 1
            right += 1

        return num_palindromes

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
            for right_bound in range(left_bound + 1, len(s)):
                num_palindromes += Solution.do_stuff(s, left_bound, right_bound, palindromes)

        for c in s:
            palindromes.append(c)

        print(palindromes)
        return len(palindromes)
        # return num_palindromes + len(s) # len(s) for single-character palindromes


def main():
    sol = Solution()

    print(sol.countSubstrings("abc"))
    print(sol.countSubstrings("aaa"))
    print(sol.countSubstrings("abcdcba"))


if __name__ == '__main__':
    main()
