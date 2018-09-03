"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 0:
            return []

        stack = [{'parens': ['('], 'open': 1, 'left': n - 1, 'right': n}]
        solutions = []

        while stack:
            p = stack.pop()
            assert(p['open'] + p['left'] == p['right'])

            if p['left'] == 0 and p['right'] == 0:
                solutions.append("".join(p['parens']))
                continue

            if p['open'] > 0:
                parens_add_right = p['parens'] + [')']

                p_add_right = {'parens': parens_add_right, 'open': p['open'] - 1, 'left': p['left'], 'right': p['right'] - 1}
                stack.append(p_add_right)

            if p['left'] > 0:
                parens_add_left = p['parens'] + ['(']

                p_add_left = {'parens': parens_add_left, 'open': p['open'] + 1, 'left': p['left'] - 1, 'right': p['right']}
                stack.append(p_add_left)

        return solutions


def main():
    sol = Solution()

    print(sol.generateParenthesis(3))


if __name__ == '__main__':
    main()
