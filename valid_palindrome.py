class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_lower = s.lower()
        phrase = "".join([c if c.isalnum() else "" for c in s_lower])

        l = 0
        r = len(phrase) - 1

        if phrase is None:
            return False

        if phrase == "":
            return True

        if len(phrase) == 1:
            return True

        while l <= r:
            if l == r:
                return True

            if phrase[l] != phrase[r]:
                return False
            l += 1
            r -= 1

        return True