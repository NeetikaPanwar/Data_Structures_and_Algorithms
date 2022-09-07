class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_groups = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            anagrams_groups[tuple(count)].append(s)

        return anagrams_groups.values()