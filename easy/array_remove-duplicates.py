class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currentNum = nums[0]
        i = 1
        j = 1
        removeCount = 0
        length = len(nums)
        while i < length:
            n = nums[i]
            if n != currentNum:
                nums[j] = nums[i]
                j += 1
                currentNum = n
            else:
                removeCount += 1

            i += 1

        return length - removeCount