class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if h < n:
            return -1

        i = 0
        while i < h - n + 1:
            if haystack[i] == needle[0]:
                isMatch = True
                for j in range(1, n):
                    if haystack[i + j] != needle[j]:
                        isMatch = False
                        break

                if isMatch:
                    return i

            i += 1

        return -1
