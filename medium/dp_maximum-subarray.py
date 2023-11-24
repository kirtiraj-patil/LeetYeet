class Solution:
    def maxSubArray(self, nums):
        currentMax = nums[-1]
        carry = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            currentSum = carry + nums[i]
            carry = max(currentSum, nums[i])
            currentMax = max(currentMax, carry)

        return currentMax


# dp solution
# class Solution:
#     def maxSubArray(self, nums: List[int], index=0, shouldSelect=False) -> int:
#         @cache
#         def findMax(index, shouldSelect):
#             if index == len(nums) - 1:
#                 return nums[index]

#             return max(nums[index], nums[index] + findMax(index+1, True), 0 if shouldSelect else findMax(index+1, False))

#         return findMax(0, False)
