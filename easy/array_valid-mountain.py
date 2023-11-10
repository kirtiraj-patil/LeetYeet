class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        index = 0
        while index < len(arr) - 1:
            if arr[index] > arr[index + 1]:
                break
            index += 1

        if index == 0 or index == len(arr) - 1:
            return False

        i = index - 1
        while i >= 0:
            if arr[i] >= arr[i + 1]:
                return False
            i -= 1

        i = index + 1
        while i < len(arr):
            if arr[i] >= arr[i - 1]:
                return False
            i += 1

        return True
