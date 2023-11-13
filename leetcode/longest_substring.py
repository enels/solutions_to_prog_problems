class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Longest substring without repeating characters
        :type s: str
        :rtype: int
        """

        previous_chars = list()
        sub_str = ""
        sub_strings = dict()
        index = 0

        for c in s:
            # new characters found
            if c not in sub_str:
                sub_str += c
            # previously stored characters found
            elif c in sub_str:
                sub_strings[index] = sub_str
                sub_str = ""
                index += 1

        # last character
        sub_strings[index] = sub_str

        # store the maximum length substring
        max_len_sub_str = 0

        for v in sub_strings.values():
            if len(v) > max_len_sub_str:
                max_len_sub_str = len(v)

        return max_len_sub_str