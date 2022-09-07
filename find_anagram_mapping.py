import collections


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_index = dict()
        anagrm_mapping = list()

        for i, num in enumerate(nums2):
            if num in nums_index:
                nums_index[num].append(i)
            else:
                nums_index[num] = collections.deque([i])

        for i, num in enumerate(nums1):
            if num in nums_index:
                anagrm_mapping.append(nums_index[num].popleft())

        return anagrm_mapping