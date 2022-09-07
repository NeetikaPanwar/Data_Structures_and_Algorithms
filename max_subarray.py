class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = -float('inf')
        nums_size = len(nums)
        curr_sum = 0

        for i in range(nums_size):
            curr_sum = curr_sum + nums[i]

            if curr_sum < nums[i]:
                curr_sum = nums[i]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum


