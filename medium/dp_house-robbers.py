class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def choose(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(nums[i] + choose(i + 2), choose(i + 1))
            return dp[i]

        return choose(0)
