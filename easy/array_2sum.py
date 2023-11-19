class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index in range(len(nums)):
            d[nums[index]] = index

        for index in range(0, len(nums)):
            req = target - nums[index]
            if req in d and d[req] != index:
                return [min(d[req], index), max(d[req], index)]
