from collections import Counter
from collections import deque
import copy


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        char_counts = Counter(s)
        chars_minus_left = deque(s[:])
        max_len = 0

        while len(chars_minus_left):
            char_counts_subtracted_from_right = Counter()

            chars_minus_left_and_right = copy.copy(chars_minus_left)

            while len(chars_minus_left_and_right) > max_len:
                char_count_dup_gen = (char_count[1] > 1 for char_count in char_counts.items())

                if not any(char_count_dup_gen):
                    max_len = len(chars_minus_left_and_right)
                else:
                    right_char = chars_minus_left_and_right[-1]
                    char_counts[right_char] -= 1
                    char_counts_subtracted_from_right[right_char] += 1
                    chars_minus_left_and_right.pop()

            char_counts += char_counts_subtracted_from_right

            char_counts[chars_minus_left[0]] -= 1
            chars_minus_left.popleft()

        return max_len


def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))

    # for i in range(1000):
    #     s.lengthOfLongestSubstring("uygevhexbfvafrqzfikrstgjlenkuooqmwvhebhhgciovanaiztbszmffbrzpfscenlkqsrzwznrcctkbnnvoaduduvtanxgc")

    print("done")


if __name__ == '__main__':
    main()
