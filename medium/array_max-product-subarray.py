import math


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        @cache
        def findMax(i, mustSelect):
            if i + 1 == len(nums):
                return [nums[i], nums[i]]

            if nums[i] == 0:
                return [0, 0] if mustSelect else findMax(i + 1, False)

            return [
                max(
                    nums[i],
                    nums[i] * findMax(i + 1, True)[0],
                    nums[i] * findMax(i + 1, True)[1],
                    -math.inf if mustSelect else findMax(i + 1, False)[0],
                ),
                min(
                    nums[i],
                    nums[i] * findMax(i + 1, True)[0],
                    nums[i] * findMax(i + 1, True)[1],
                ),
            ]

        return max(findMax(0, False))


# Its all about having odd or even numbers of negative integers. if the negative numbers are even, then the first pass will give the solution. If the negative numbers are odd, the second pass will give the solution.

# class Solution {
#     public int maxProduct(int[] nums) {
#         int prod = 1;
#         int result = Integer.MIN_VALUE;

#         for (int i = 0; i < nums.length; i++) {
#             prod = prod * nums[i];
#             result = Math.max(prod, result);
#             if(prod == 0) {
#                 prod = 1;
#             }
#         }
#         prod = 1;

#         for (int i = nums.length - 1; i >= 0; i--) {
#             prod = prod * nums[i];
#             result = Math.max(prod, result);
#             if(prod == 0) {
#                 prod = 1;
#             }
#         }
#         return result;
#     }
# }
