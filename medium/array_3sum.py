class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            # if nums only have positive numbers or
            # nums only have negative numbers, there are no triplets
            if nums[0] > 0 or nums[-1] < 0:
                break

            # to avoid duplicates, skip over same numbers as the array is sorted
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # check for combinations in the remaining part of the array
            start = i + 1
            end = len(nums) - 1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                # if sum is negative, we need a greater number
                if s < 0:
                    start += 1

                # if sum is positive, we need a lower number
                elif s > 0:
                    end -= 1

                # triplet found, append to res
                # skip over equal numbers near start and near end
                else:
                    res.append([nums[i], nums[start], nums[end]])
                    lastLow, lastHigh = nums[start], nums[end]
                    while start < end and nums[start] == lastLow:
                        start += 1
                    while start < end and nums[end] == lastHigh:
                        end -= 1

        return res
