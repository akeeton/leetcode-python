from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # for char in chars:
        #     char_counts[char] = 1 if char not in char_counts else char_counts[char] + 1

        chars = s
        char_counts_base = Counter(chars)
        max_len = 0
        # max_len_substring = ""

        for left_index, start_char in enumerate(chars):
            if left_index > 0:
                char_counts_base[chars[left_index - 1]] -= 1

            char_counts = char_counts_base.copy()

            for right_index in reversed(range(left_index, len(chars))):
                substring = chars[left_index:right_index + 1]

                if len(substring) < max_len:
                    break

                char_count_dup_gen = (char_count[1] > 1 for char_count in char_counts.items())

                if not any(char_count_dup_gen) and len(substring) > max_len:
                    max_len = len(substring)
                    # max_len_substring = substring

                char_counts[substring[-1]] -= 1

                # print(substring)
                # print(char_counts)
                # print(list(char_count_dup_gen))

        # print("Max substring: '{}'".format(max_len_substring))
        return max_len


def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))


if __name__ == '__main__':
    main()
