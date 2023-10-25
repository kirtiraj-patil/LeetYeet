class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        firstW = strs[0]
        lastW = strs[-1]

        i = 0
        minRange = min(len(firstW), len(lastW))
        while i < minRange and firstW[i] == lastW[i]:
            i += 1

        return firstW[0:i]