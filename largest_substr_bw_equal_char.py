class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        chars_win_len = dict()
        max_len = -1

        for i, c in enumerate(s):

            if c in chars_win_len:
                win_len = i - chars_win_len[c] - 1
                max_len = max(win_len, max_len)

            else:
                chars_win_len[c] = i

        return max_len

