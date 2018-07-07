class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # chars = list(s)
        chars = s
        max_len = 0
        max_len_substring = ""
        for left_index, start_char in enumerate(chars):
            for right_index in reversed(range(left_index + 1, len(chars))):
                substring = chars[left_index:right_index + 1]
                char_counts = {}

                for char in substring:
                    char_counts[char] = 1 if char not in char_counts else char_counts[char] + 1

                char_count_dup_gen = (char_count[1] > 1 for char_count in char_counts.items())

                if not any(char_count_dup_gen) and len(substring) > max_len:
                    max_len = len(substring)
                    max_len_substring = substring

                # print(substring)
                # print(char_counts)
                # print(list(char_count_dup_gen))

        print("Max substring: '{}'".format(max_len_substring))
        return max_len


def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))


if __name__ == '__main__':
    main()
