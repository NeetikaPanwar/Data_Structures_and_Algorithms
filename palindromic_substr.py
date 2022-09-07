class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)

        palindromes = list()
        count_pals = 0

        for i in range(size):
            palindromes.append([0 for j in range(size)])

        i = 0
        j = 0
        curr_i = i + 1

        while i < size and j < size:
            if i == j:
                palindromes[i][j] = 1
                count_pals += 1
            elif j == i + 1:
                if s[i] == s[j]:
                    count_pals += 1
                    palindromes[i][j] = 1
            elif j > i:
                if s[i] == s[j] and palindromes[i + 1][j - 1] == 1:
                    count_pals += 1
                    palindromes[i][j] = 1

            if i == (size - 1) or j == (size - 1):
                i = 0
                j = curr_i
                curr_i += 1
            elif i < (size - 1):
                i += 1
                j += 1

        return count_pals

