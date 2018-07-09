from collections import deque


class Solution:
    @staticmethod
    def is_open_paren(paren):
        return paren == '(' or paren == '[' or paren == '{'

    @staticmethod
    def is_closed_paren(paren):
        return paren == ')' or paren == ']' or paren == '}'

    @staticmethod
    def is_paren(paren):
        return Solution.is_open_paren(paren) or Solution.is_closed_paren(paren)

    @staticmethod
    def open_paren_from_closed_paren(paren):
        assert(Solution.is_closed_paren(paren))
        return {')': '(', ']': '[', '}': '{'}[paren]

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        parens_stack = deque()
        for paren in s:
            if Solution.is_open_paren(paren):
                parens_stack.append(paren)
            elif Solution.is_closed_paren(paren):
                try:
                    paren_open = parens_stack.pop()
                except IndexError:
                    return False

                if paren_open != Solution.open_paren_from_closed_paren(paren):
                    return False
            else:
                return False

        return len(parens_stack) == 0


def main():
    sol = Solution()
    print(sol.isValid("()"))
    print(sol.isValid("()[]{}"))
    print(sol.isValid("(]"))
    print(sol.isValid("([)]"))
    print(sol.isValid("{[]}"))


if __name__ == '__main__':
    main()
