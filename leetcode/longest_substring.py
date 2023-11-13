class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        previous_chars = list()
        sub_str = ""
        sub_strings = dict()
        index = 0

        current_index = -1
        for c in s:
            current_index += 1
            # new characters found
            if c not in sub_str:
                sub_str += c
            # previously stored characters found
            elif c in sub_str:
                sub_strings[index] = sub_str
                # store the last character of the last substring
                previous_c = sub_str[len(sub_str) - 1]
                # if they are the same assign same character
                if previous_c == c:
                    sub_str = c
                # if they are different, store it in the substring
                else:
                    sub_str += c
                    new_sub_str = ""
                    # iterate thru the new substring and store it as the current
                    # substring stating from the current index of the current sub string
                    sub_index = index + 1
                    # loop until current character c is not in the remaining part
                    # part of the string
                    # skip the substring between the next character string s
                    # and the current character position
                    while True:
                        # if c is not within the next character string and the end
                        # of the current character position
                        if c not in sub_str[sub_index:current_index]:
                            sub_str = sub_str[sub_index:]
                            # break out of while loop
                            break
                        # move to next substring character
                        else:
                            sub_index += 1
                            sub_str = sub_str[sub_index:]

                # index of each substring obtained stored in the dict
                index += 1

        # last character
        sub_strings[index] = sub_str

        # store the maximum length substring
        max_len_sub_str = 0

        # get the substring with the highest length
        for v in sub_strings.values():
            if len(v) > max_len_sub_str:
                max_len_sub_str = len(v)

        return max_len_sub_str