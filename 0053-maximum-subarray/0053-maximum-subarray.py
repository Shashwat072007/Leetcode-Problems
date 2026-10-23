class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = best_sum = nums[0]
        for n in nums[1:]:
            current_sum = max(n , current_sum + n)
            best_sum = max(best_sum , current_sum)
        return best_sum 