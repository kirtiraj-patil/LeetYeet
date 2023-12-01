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
