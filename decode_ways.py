class Solution:

    def numDecodings(self, s: str) -> int:
        size = len(s)

        decodings = [0 for _ in range(size + 1)]

        decodings[0] = 1

        decodings[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(decodings)):

            if s[i - 1] != '0':
                decodings[i] = decodings[i - 1]

            two_digit = int(s[i - 2: i])
            if two_digit >= 10 and two_digit <= 26:
                decodings[i] += decodings[i - 2]

        return decodings[size]