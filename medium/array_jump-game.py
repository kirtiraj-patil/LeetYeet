class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastReachableIndex = len(nums) - 1
        for i in range(lastReachableIndex - 1, -1, -1):
            if i + nums[i] >= lastReachableIndex:
                lastReachableIndex = i

        return lastReachableIndex == 0
