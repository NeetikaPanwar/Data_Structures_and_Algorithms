class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        sorted_intervals = sorted(intervals, key=itemgetter(0))

        merged = []

        for interval in sorted_intervals:

            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged