class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_freq = {}

        if len(t) != len(s):
            return False

        if s is None or t is None:
            return False

        for i in range(len(s)):
            s_char_freq[s[i]] = s_char_freq.get(s[i], 0) + 1

        for j in range(len(t)):
            if t[j] not in s_char_freq or s_char_freq[t[j]] <= 0:
                return False
            s_char_freq[t[j]] -= 1

        return True